#!/usr/bin/python

from secrets import *
import tweepy
import csv
import ipdb
import json


# twitter setup #
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

#api = tweepy.API(auth)

# post a tweet to timeline
# tweet = "Hello World! I made a Twitter Bot!";
# api.update_status(tweet)

# #print all tweets from users timeline to terminal
# example of method parameters -->> api.home_timeline([since_id][, max_id][, count][, page])
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
# csvFile = open('ua.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#snow",count=100,
                           lang="en",
                           since="2017-04-03").items():
    ipdb.set_trace()
    print (tweet.created_at, tweet.text)
    json_data = tweet.text
    json_data_geo = tweet.geo
    print(json_data)
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
