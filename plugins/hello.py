# -*- coding: utf-8 -*-

import json
import os
import requests

DISCOURSE_API_KEY = os.environ['DISCOURSE_API_KEY']

WELCOME_TEXT = """
> Welcome to *Hacklag* community! :tada:
> We are using *Slack* and *Discourse* Forum to collaborate. This is short guide what is where on our Slack Channels and Forum:
> \n
"""

def prep_category(cat):
  return {
    "color": cat['color'],
    "title": cat['name'],
    "title_link": cat['forum_url'],
    "text": '%s #%s | <%s|%s>' % (cat['desc'], cat['slack_channel'], cat['forum_url'], cat['name']),
  }


def get_categories():
  categories_url = 'https://forum.hacklag.org/categories.json?api_key=%s' % DISCOURSE_API_KEY
  categories = requests.get(categories_url).json()

  categories_list = []
  for category in categories['category_list']['categories']:
    if not category['read_restricted']:
      categories_list.append(
          prep_category({
            'name': category['name'],
            'slack_channel': category['slug'],
            'desc': category['description'],
            'forum_url': "https://forum.hacklag.org/c/%s" % category['slug'],
            'color': '#' + category['color'],
          })
      )
  return categories_list

def process_message(data, ctx):
  channel = data["channel"]
  if data.has_key("text"):
    text = data["text"]

    if text.startswith("<@U0Q74DWT1>"):
      if "welcome" in text:
        ctx.api_call(
          "chat.postMessage",
          channel=data['user'],
          text=WELCOME_TEXT,
          link_names=1,
          as_user=True,
          attachments=json.dumps(get_categories())
        )

    if 'subtype' in data and data['subtype'] == 'channel_join':
      if ctx.server.channels.find(data['channel']).name == "test":
          ctx.api_call(
            "chat.postMessage",
            channel=data['user'],
            text=WELCOME_TEXT,
            link_names=1,
            as_user=True,
            attachments=json.dumps(get_categories())
          )

