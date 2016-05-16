# -*- coding: utf-8 -*-
import time
import json
import meeting

crontable = []
outputs = []

#crontable.append([86400, "check_events"])

def is_event_in_next(days):
  events_list = meeting.get_events('Upcoming',days)
  if len(events_list) > 0:
    return events_list

def check_events():
  days=21
  if is_event_in_next(days):
    event_count=json.loads(is_event_in_next(days))
    outputs.append(["C0NTENR9B", 'In next %d days, :hackbat: Hacklag will organize %d meetings. \n Any time, you can ask me about the details by using the `meeting next` command.' % (days, len(event_count))])
