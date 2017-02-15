# -*- coding: utf-8 -*-
import yaml
import re
import string

from urlparser import parseText

MENTION = re.compile("@[A-Za-z0-9_]{1,16}", re.IGNORECASE)
HASHTAG = re.compile("#[A-Za-z0-9]+", re.IGNORECASE)

def writeToYml(path, data):
    with open(path, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False, allow_unicode=True, encoding=('utf-8'))

def removeHashtags(text, hashtags):
    if hashtags is None:
        return text

    # not replacing #jallikattu alone
    pattern = re.compile("#jallikattu", re.IGNORECASE)

    # replacing #jallikattu as jallikattu in text
    text = pattern.sub("jallikattu", text)

    regex = ""
    for tag in hashtags.split(" "):
        regex += tag + "|"

    regex = "(" + regex + ")"
    pattern = re.compile(regex, re.I)

    return pattern.sub("", text)

def removeMentions(text):
    return ' '.join(filter(lambda x: x not in MENTION.findall(text), text.split()))

def removePunctuation(text):
    return "".join([ch for ch in text if ch not in string.punctuation])

def tokenize(text, hashtags):
    text = removeMentions(text)
    text = removeHashtags(text, hashtags)
    return removePunctuation(text)

def normalizeText(text, hashtags=None):
    text = text.encode('utf-8')

    if text[-3:] == "…":
        text = text[:-3]

    text.replace('pic.twitter.com', 'https://pic.twitter.com')
    urls = parseText(text)
    for url in urls:
        text = text.replace(url[1], '')

    text = text.replace('https', '')
    text = text.replace('http', '')

    return tokenize(text.lower(), hashtags)
