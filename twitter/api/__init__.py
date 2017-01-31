# -*- coding: utf-8 -*-
import got
import os
import yaml

PWDPATH = os.path.abspath(__file__)
apipath = os.path.dirname(PWDPATH)
YMLPATH = os.path.dirname(apipath) + '/data/data.yml'

data = []
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#jallikattu, OR #jallikattubill, OR #ammendpca').setSince("2017-01-07").setUntil("2017-01-21").setMaxTweets(10)
for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
    data.append({
        'id': tweet.id,
        'text': tweet.text.encode('utf-8'),
        'username': tweet.username,
        'permalink': tweet.permalink,
        'date': tweet.date,
        'retweets': tweet.retweets,
        'favorites': tweet.favorites,
        'hashtags': tweet.hashtags,
        'geo': tweet.geo
    })

with open(YMLPATH, 'w') as outfile:
    yaml.safe_dump(data, outfile, default_flow_style=False, allow_unicode=True, encoding=('utf-8'))
