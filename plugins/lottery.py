# -*- coding: utf-8 -*-
import os
import requests
from random import randint

def process_message(data, ctx):
    channel = data["channel"]
    text = data["text"]

    if text.startswith("!lottery"):
      ctx.api_call(
          "chat.postMessage",
          channel="C0QA34UQ7",
          text="Lottery initiated by <@"+data['user']+"> \n Generating number from range 1 to 10... \n Number is: `"+str(randint(1, 10))+"`",
          link_names=1,
          username='HackBat',
          icon_emoji=':hackbat2:'
      )
