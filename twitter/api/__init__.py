# -*- coding: utf-8 -*-
import got
import os
import yaml

from paths import POSPATH, NEGPATH
from writer import writeToYml, normalizeText

data = []
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#banjallikattu').setSince("2017-01-07").setUntil("2017-01-21").setMaxTweets(1500)
for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
    txt = normalizeText(tweet.text, hashtags=tweet.hashtags)

    data.append({
        'id': tweet.id,
        'text_full': tweet.text.encode('utf-8'),
        'text': txt,
        'username': tweet.username,
        'permalink': tweet.permalink,
        'date': tweet.date,
        'retweets': tweet.retweets,
        'favorites': tweet.favorites,
        'hashtags': tweet.hashtags,
        'geo': tweet.geo,
        'sent': 0
    })

writeToYml(NEGPATH, data)
