# import tweepy
# import random
#
# from authorization_tokens import *
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)
#
# message = ""

#Option 5: Basic search
# search_results = api.search(q="Bieber filter:safe", lang="en")
# random_tweet= random.choice(search_results)
#print( dir(random_tweet) )
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(random_tweet._json)

# text = random_tweet.full_text
# message = text.replace("Bieber", "Bieber at the met gala,")
# print(message)

# #Option 6: Mentions
# mentions = api.mentions_timeline()
# mention_tweet = random.choice(mentions)
# thanks = " yes!!!"
# message = "@" + mention_tweet.user.screen_name + thanks
#
# api.update_status(message)
# print("Done.")
