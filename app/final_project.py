import time
import datetime
from datetime import datetime as dt
import json
import requests
import tweepy
from authorization_tokens import *
import os, sys
import random

def import_old_weather():
    timestamp_map = {}
    filename = os.path.join(sys.path[0], "old_temp.json")
    with open(filename, "r") as f:
        data = json.load(f)
        for obj in data:
            timestamp = obj["dt_iso"][:10]
            timestamp_map[timestamp] = obj
    return timestamp_map

def get_weather_ten_years_ago():
    ts_map = import_old_weather()
    today = dt.utcnow().date()
    year = str(today.year - 10)
    month = str(today.month).zfill(2)
    day = str(today.day).zfill(2)
    key = '-'.join([year, month, day])
    return ts_map[key]['main']['temp']

def get_today_data():
    api_key = "affda21f806478a8d6aae414fd6864fb"
    url = "https://api.openweathermap.org/data/2.5/weather?q=New%20York%20City&appid={}".format(api_key)
    r = requests.get(url)
    today = r.json()
    temp = float(today["main"]["temp"])
    celsius = temp - 273.15
    return celsius

def post_to_twitter():
    ten_years_ago = get_weather_ten_years_ago()
    today = get_today_data()
    message = "Today's weather is {} and it was {} 10 years ago. ".format(today, ten_years_ago)
    phrase_list = ["Save the Earth!","There is no planet B", "It's getting too warm.", "Time for the planet to cool down..."]
    message = message + random.choice(phrase_list)
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)
    

post_to_twitter()
