# -*- coding: utf-8 -*-
import os
import requests
from random import randint

def process_message(data, ctx):
  channel = data["channel"]
  text = data["text"]
  if text.startswith("<@U0MBV30AC>"):
    if "youtube" in text:
      ctx.api_call(
          "chat.postMessage",
          channel=data["channel"],
          text="<https://www.youtube.com/watch?v=dQw4w9WgXcQ>",
          link_names=1,
          username='HackBat',
          icon_emoji=':hackbat2:',
          unfurl_media='true'
      )
