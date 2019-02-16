#!/usr/bin/env python

import sys
from datetime import datetime, date, time
import secrets
import os

sys.path.insert(0, 'deps')
import twitter

def elapsed(now = datetime.now()):
    # TODO: UTC lol

    # 0%
    start = datetime(2001, 1, 1, 0, 0, 0)

    # 100%
    end = datetime(2100, 12, 31, 23, 59, 59)

    full = end - start

    # now = datetime(2020, 1, 1, 0, 0, 0)

    return ( (now - start).total_seconds() / full.total_seconds() ) * 100

def bar(elapsed):
    on = ( 15 * elapsed ) / 100
    off = 15 - on
    bar_on = u'\u2593' * int(on)
    bar_off = u'\u2591' * int(off)
    return '[' + bar_on + bar_off + ']'



def main():
    elapsed = elapsed()
    text = bar(elapsed) + ' ' + "%.4f" % elapsed + '%'

    if "TWEET" in os.environ:
        api = twitter.Api(consumer_key=secrets.consumer_key,
                          consumer_secret=secrets.consumer_secret,
                          access_token_key=secrets.access_token_key,
                          access_token_secret=secrets.access_token_secret)
        status = api.PostUpdate( text )

    print text

