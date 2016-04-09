#!/bin/bash
rsync -v plugins/* $BOT_USERNAME@$BOT_HOST:/home/$BOT_USERNAME/hacklag-bot/plugins
rsync -pv --chmod=+rwx rtmbot.py -z $BOT_USERNAME@$BOT_HOST:/home/$BOT_USERNAME/hacklag-bot/
rsync -pv --chmod=+rwx startup.sh -z $BOT_USERNAME@$BOT_HOST:/home/$BOT_USERNAME/hacklag-bot/
