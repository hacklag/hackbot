#!/bin/bash
echo "DEBUG: True," > /src/rtmbot/rtmbot.conf
echo "LOGFILE: 'logs.log'" >> /src/rtmbot/rtmbot.conf
SLACK_TOKEN=$SLACK_TOKEN
DISCOURSE_API_KEY=$DISCOURSE_API_KEY
exec /src/rtmbot/rtmbot.py
