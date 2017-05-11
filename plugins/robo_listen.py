# -*- coding:utf-8 -*-

from slackbot.bot import listen_to
from weather_api import weather_response
@listen_to('諦めたら')
@listen_to('あきらめたら')
def anzai(message):
    message.send('そこで試合終了ですよ')

@listen_to('いいですか')
def reaction(message):
    message.react('+1')
@listen_to('天気')
def weather(message):
    message.send(weather_response())
