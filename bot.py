#!/usr/bin/python

from secrets import *
import tweepy

# twitter setup #
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

tweet = "Hello World! I made a Twitter Bot!";

api.update_status(tweet)
