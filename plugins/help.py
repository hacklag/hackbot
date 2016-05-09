# -*- coding: utf-8 -*-
import os
import requests

commands = [
  '`help` - get help message with commands list',
  '`lottery` - run simple lottery on channel',
  '`youtube` - simple link to YT movie',
  '`welcome` - print welcome message',
  '`meeting next` - print information about upcoming events',
  '`meeting prev` - print information about past events'
];

def print_commands():
    message = "";
    for i in range(len(commands)):
      message+=commands[i]+"\n"
    return message;

def process_message(data, ctx):
    channel = data["channel"]
    text = data["text"]

    if text.startswith("<@U0Q74DWT1>"):
      if "help" in text:
        ctx.api_call(
            "chat.postMessage",
            channel=data['user'],
            text="Welcome to my lounge, dear <@"+data['user']+"> \n Currently working commands: \n"+print_commands(),
            link_names=1,
            as_user="true"
        )
