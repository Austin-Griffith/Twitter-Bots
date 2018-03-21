#!/usr/bin/env python
from secrets import *
import time
from gnippy import PowerTrackClient

# Define a callback
def callback(activity):
    print(activity)

# Create the client
client = PowerTrackClient(callback, url='https://gnip-api.twitter.com/rules/powertrack/accounts/greg-students/publishers/twitter/prod.json', auth=('austin.griffith@colorado.edu', 'Vicki1957!'))
client.connect()

# Wait for 2 minutes and then disconnect
#check what 2 mintues of tweets gives as output
time.sleep(20)
client.disconnect()
