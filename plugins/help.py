# -*- coding: utf-8 -*-
import os
import requests
import json
import random

commands = """[
  {
    "title": "help",
    "text": "Get help message with commands list"
  },
  {
    "title": "lottery",
    "text": "Run simple lottery on channel"
  },
  {
    "title": "meeting <type>",
    "text": "Print information about meetups, for type use: \\n*next* - get info about upcoming events \\n*prev* - get info about past events"
  },
  {
    "title": "welcome",
    "text": "Print welcome message containing basic forum information"
  },
  {
    "title": "youtube",
    "text": "Print YouTube example movie"
  }
]"""

HELP_TEXT="""
> Welcome to *Hackbot* service!
> Full command list can be found below:
> \n
"""

def prep_command(command):
  return {
    "color": '#%06x' % random.randint(0, 0xFFFFFF),
    "title": command['title'],
    "text": command['text'],
    "mrkdwn_in": [
      "text",
      "pretext"
    ]
  }

def get_commands():
  json_data = json.loads(commands)
  commands_list = []

  for current in json_data:
    commands_list.append(
      prep_command({
        'title': current['title'],
        'text': current['text']
      })
    )

  return json.dumps(commands_list)

def process_message(data, ctx):
  channel = data["channel"]
  text = data["text"]

  if text.startswith("<@U0Q74DWT1>"):
    if "help" in text:
      ctx.api_call(
        "chat.postMessage",
        channel=data['user'],
        text=HELP_TEXT,
        link_names=1,
        as_user=True,
        attachments=get_commands()
      )
