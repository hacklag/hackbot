FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y python-pip

WORKDIR /src/rtmbot
COPY . /src/rtmbot

RUN pip install -r requirements.txt

ENV DEV 'False'

# Create a startup.sh bash script
RUN echo '#!/bin/bash\n echo "DEBUG: False \nDEV: $DEV" >> /src/rtmbot/rtmbot.conf \nSLACK_TOKEN=$SLACK_TOKEN \nDISCOURSE_API_KEY=$DISCOURSE_API_KEY \nexec /src/rtmbot/rtmbot.py >> startup.sh && \
  chmod +x startup.sh && \
  chmod +x /src/rtmbot/rtmbot.py

ENTRYPOINT ["/src/rtmbot/startup.sh"]
