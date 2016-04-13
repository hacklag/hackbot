# -*- coding: utf-8 -*-
import os
import requests
import json
from random import randint

def process_message(data, ctx):
  channel = data["channel"]
  text = data["text"]

  generated_number = randint(1, 10)
  generated_color = "#ff0000"

  if 4 <= generated_number < 7:
    generated_color = "#ff7700"
  elif 7 <= generated_number < 11:
    generated_color = "#00ff00"

  attach = [{"color": generated_color, "title": "Generating number from range 1 to 10... ","text": "Number: "+str(generated_number)}]

  if text.startswith("<@U0Q74DWT1>"):
    if "lottery" in text:
      ctx.api_call(
          "chat.postMessage",
          channel=data["channel"],
          text="Lottery initiated by <@"+data['user']+">",
          link_names=1,
          as_user="true",
          attachments=json.dumps(attach)
      )
