#!/usr/bin/python

from secrets import *
import searchtweets
import ipdb
import json
import pprint
from searchtweets import *

enterprise_search_args = load_credentials("creds.yaml",
                                          yaml_key="search_tweets_enterprise",
                                          env_overwrite=False)
print(enterprise_search_args)
print('\n')

#rule = gen_rule_payload("is raining", from_date="2018-04-03", to_date="2018-04-04", results_per_call=100)
#rule = {"query":"raining","maxResults":10}

rule = {"query":"raining","maxResults":10,"toDate":"201710300000","fromDate":"201709010000"}

print(rule)
print('\n')
print('\n')

tweets = collect_results(rule,
                         max_results=10,
                         result_stream_args=enterprise_search_args)

rs = ResultStream(rule_payload=rule,
                  max_results=100,
                  max_pages=1,
                  **enterprise_search_args)

pprint.pprint(rs)

pprint.pprint(tweets)

#print(tweet.all_text, end='\n\n') for tweet in tweets[0:500] ;
