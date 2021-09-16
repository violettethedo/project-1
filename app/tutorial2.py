import tweepy

from authorization_tokens import *

import random

message = ""
phrase_list = ["Hi my name is Vio.","I am a girl.", "I am from Belgium", "I am 19.", "I'm a boy", "I live in New York", "I like Chickfila"]
message = random.choice(phrase_list)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
