# -*- coding: utf-8 -*-
import os
import requests

def process_message(data, ctx):
  channel = data["channel"]
  text = data["text"]
  if text.startswith("<@U0Q74DWT1>"):
    if "youtube" in text:
      ctx.api_call(
        "chat.postMessage",
        channel=data["channel"],
        text="<http://www.youtube.com/watch?v=6v2L2UGZJAM>",
        unfurl_media=True,
        unfurl_links=True,
        as_user=True
      )
