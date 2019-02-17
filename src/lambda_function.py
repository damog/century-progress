#!/usr/bin/env python

import sys
import json
from datetime import datetime, date, time
import secrets
import os

#sys.path.insert(0, 'deps')
import twitter


def lambda_handler(event = None, context = None):
    # TODO: UTC lol

    start = datetime(2001, 1, 1, 0, 0, 0)
    end = datetime(2100, 12, 31, 23, 59, 59)

    full = end - start
    elapsed = ( (datetime.now() - start).total_seconds() / full.total_seconds() ) * 100

    on = ( 15 * elapsed ) / 100
    off = 15 - on
    bar_on = u'\u2593' * int(on)
    bar_off = u'\u2591' * int(off)
    text = '[' + bar_on + bar_off + ']' + ' ' + "%.4f" % elapsed + '%'

    if "TWEET" in os.environ:
        api = twitter.Api(consumer_key=secrets.consumer_key,
                          consumer_secret=secrets.consumer_secret,
                          access_token_key=secrets.access_token_key,
                          access_token_secret=secrets.access_token_secret)
        status = api.PostUpdate( text )

    return { 'message' : text }

