#!/bin/bash
rsync plugins/* $BOT_USERNAME@$BOT_HOST:/home/$BOT_USERNAME/hacklag-bot/plugins
rsync -p --chmod=+rwx rtmbot.py -z $BOT_USERNAME@$BOT_HOST:/home/$BOT_USERNAME/hacklag-bot/
rsync -p --chmod=+rwx startup.sh -z $BOT_USERNAME@$BOT_HOST:/home/$BOT_USERNAME/hacklag-bot/
