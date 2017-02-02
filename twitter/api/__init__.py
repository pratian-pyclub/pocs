# -*- coding: utf-8 -*-
import got
import os
import yaml

from paths import POSPATH, NEGPATH
from writer import writeToYml, normalizeText

data = []
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#banjallikattu').setSince("2017-01-07").setUntil("2017-01-21").setMaxTweets(10)
for i in range(7,22):
    if i == 7:
        since_day = "06"
        until_day = "07"
    elif i == 8:
        since_day = "07"
        until_day = "08"
    elif i == 9:
        since_day = "08"
        until_day = "09"
    else:
        if i == 10:
            since_day = "09"
        else:
            since_day = str(i-1)
        until_day = str(i)

    print since_day
    print until_day
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#banjallikattu').setSince("2017-01-"+since_day).setUntil("2017-01-"+until_day).setMaxTweets(10)
    
    for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
        txt = normalizeText(tweet.text, hashtags=tweet.hashtags)
        date = str(tweet.date)
        date = date.split(' ')[0]
        print date
        data.append({
            'id': tweet.id,
            'text_full': tweet.text.encode('utf-8'),
            'text': txt,
            'username': tweet.username,
            'permalink': tweet.permalink,
            'date': date,
            'retweets': tweet.retweets,
            'favorites': tweet.favorites,
            'hashtags': tweet.hashtags,
            'geo': tweet.geo,
            'sent': 0
        })

    writeToYml(NEGPATH, data)