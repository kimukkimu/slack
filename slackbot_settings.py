# -*- coding: utf-8 -*-
import os

#API_TOKEN = "xoxb-181466184758-vwvQStW1hIwP4RH9BjiLHhj1"
API_TOKEN = os.environ.get('SLACKBOT_API','')

default_reply = "Hey, I'm on Heroku"

PLUGINS = ['plugins',]
