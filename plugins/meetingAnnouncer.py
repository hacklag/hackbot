# -*- coding: utf-8 -*-
import time
import json
import meeting

crontable = []
outputs = []

crontable.append([86400, "check_events"])

def is_event_in_next(days):
  events_list = meeting.get_events('upcoming',days)
  if len(events_list) > 1:
    return json.dumps(events_list)

def check_events():
  outputs.append(["C0NTENR9B",is_event_in_next(14)])
