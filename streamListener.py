#!/usr/bin/python

from secrets import *
import tweepy
import json
import pandas
import pprint
import ipdb

# twitter setup #
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class tweetListener(tweepy.StreamListener):

    def on_status(self, status):
        # ipdb.set_trace()
        if not status.geo:
            print(status.geo)
            return
        pprint.pprint(status._json)
        #print(status)               #prints tweet object in JSON data form to terminal
        # print(status.source)

    def on_error(self,status):      #error handling for API requests
        if status_code == 420:
                return False

tweetListener = tweetListener()
myStream = tweepy.Stream(auth = api.auth, listener=tweetListener)

myStream.filter(track=['snow'])     #filters by keyword within the tweet
