# -*- coding: utf-8 -*-
import got
from collections import Counter
import matplotlib.pyplot as plt
from paths import DATAPATH
from writer import normalizeText
from random import choice

profiles = ['ndtv','htTweets','timesofindia','zeenews','newsintamilnadu','outlookindia','ibtimes_india','the_hindu','TheEconomist','CNN','BBCWorld',
            'indiaToday','firstpost','HuffPostIndia']
# profiles = ['ndtv','htTweets']
data= []
for username in profiles:
    print username+'...'
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setQuerySearch('peta OR jallikattu').setSince("2017-01-07").setUntil("2017-01-21")
    #tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#banjallikattu').setSince("2017-01-07").setUntil("2017-01-21").setMaxTweets(1)
    for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
        txt = normalizeText(tweet.text, hashtags=tweet.hashtags)

        data.append([
            tweet.username,
            tweet.date.strftime('%d/%m/%Y')
        ])

colors = ['#FF3352','#FF6B33','#C70039','#261DDA']
results = {}
for k, v in data:
    if k in results: results[k].append(v)
    else: results[k] = [v]

dates = []

for i in range(7,22):
    if i < 10:
        dates.append('0'+str(i)+'/01/2017')
    else:
        dates.append(str(i)+'/01/2017')

for key in results:
    x,y,values = [], [], []
    a = Counter(results[key])
    for k in sorted(a.iterkeys()):
        x.append(k)
        y.append(a[k])

    for adate in dates:
        if adate in x:
            values.append(y.pop())
        else:
            values.append(0)

    Y = range(len(dates))
    plt.bar(Y,values,color=choice(colors),align='center')
    plt.title('Tweets on Jallikattu by @'+ key)
    plt.ylabel('No of related tweets')
    plt.xticks(Y,dates,rotation=45)

    plt.show()
