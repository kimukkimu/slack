# -*- coding:utf-8 -*-

from slackbot.bot import listen_to

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


import requests
import pprint



def weather_response():
    api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=260010'
    weather_date = requests.get(api_url).json()

    response = weather_date['title'] + '\n'
    for forecasts in weather_date['forecasts']:
        response += forecasts['dateLabel'] + 'の天気は、' + forecasts['telop'] + '\n'
    return response
