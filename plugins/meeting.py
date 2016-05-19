# -*- coding: utf-8 -*-
import json
import os
import requests
import random
import re
from datetime import datetime, timedelta
from pytz import timezone

def prep_main_text(meeting_type):
  return """> %s *Hacklag* Meetup community meetings :calendar:""" % str(meeting_type)

def prep_event(event):
  return {
    "color": '#%06x' % random.randint(0, 0xFFFFFF),
    "title": event['name'],
    "title_link": event['event_url'],
    "text": ':alarm_clock: *Date:* %s \n :world_map: *Place:* %s ( %s, :flag-%s:%s ) \n :busts_in_silhouette: *Attendants count:* %d \n:spiral_note_pad: *Description:* \n %s \n' % (event['time'],event['venue_name'],event['venue_city'],event['venue_country'],event['venue_localized'],event['yes_rsvp_count'],event['description']),
    "mrkdwn_in": [
      "text",
      "pretext"
    ]
  }

def get_events(meeting_type,dateOffset=0):
  events_url = 'http://api.meetup.com/2/events?&group_urlname=Białystok-Hacklag-Foundation-Meetup&status='+str(meeting_type).lower()
  events = requests.get(events_url).json()

  events_list = []
  for event in events['results']:
    local_utc = timezone('UTC')
    event_time = local_utc.localize(datetime.fromtimestamp(event['time']/1000))
    event_time = event_time.astimezone(timezone('Poland'))

    if dateOffset == 0 or (event_time.astimezone(local_utc) - timedelta(days=dateOffset) < local_utc.localize(datetime.now())):
      events_list.append(
        prep_event({
          'name': event['name'],
          'event_url': event['event_url'],
          'description': re.sub('<[^<]+?>', '', event['description']),
          'time': event_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'),
          'yes_rsvp_count': event['yes_rsvp_count'],
          'venue_name': event['venue']['name'],
          'venue_city': event['venue']['city'],
          'venue_localized': event['venue']['localized_country_name'],
          'venue_country': event['venue']['country']
        })
      )

  return json.dumps(events_list)

def process_message(data, ctx):
  channel = data["channel"]
  if data.has_key("text"):
    text = data["text"]
    if text.startswith("<@U0Q74DWT1>"):
      if "meeting" in text:
        if "next" in text:
          ctx.api_call(
            "chat.postMessage",
            channel=data["channel"],
            text=prep_main_text('Upcoming'),
            link_names=1,
            as_user=True,
            attachments=get_events('Upcoming')
          )
        elif "prev" in text:
          ctx.api_call(
            "chat.postMessage",
            channel=data["channel"],
            text=prep_main_text('Past'),
            link_names=1,
            as_user=True,
            attachments=get_events('Past')
          )


