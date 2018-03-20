#!/usr/bin/python

import json
import pprint

with open('streamData.txt', 'r') as file:
    json_data = json.load(file.read())

pprint.pprint(json_data)
