FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y python-pip

WORKDIR /src/rtmbot
COPY . /src/rtmbot

RUN pip install -r requirements.txt

ENV DEV 'False'

# Create a startup.sh bash script
RUN chmod +x startup.sh

RUN chmod +x /src/rtmbot/rtmbot.py

ENTRYPOINT ["/src/rtmbot/startup.sh"]
