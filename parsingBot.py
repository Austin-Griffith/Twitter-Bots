#!/usr/bin/python

from secrets import *

import random
import tweepy

# twitter setup
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#get intro text
introText = open('intro.txt')
introList = introText.readlines()
introNum = random.randrange(len(introList))
intro = introList[introNum]

#get outroText
outroText = open('outro.txt')
outroList = outroText.readlines()
outroNum = random.randrange(len(outroList))
outro = outroList[outroNum]

tweet = intro + " " + outro
tweet = tweet.replace('\n', '')

api.update_status(tweet)
