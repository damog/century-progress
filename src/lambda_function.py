#!/usr/bin/env python

# LICENSE:
#   http://www.wtfpl.net/about/

import sys
import json
from datetime import datetime, date, time
import secrets
import os

import tweetpony

def lambda_handler(event = None, context = None):
    # TODO: UTC lol
    start   = datetime(2001, 1, 1, 0, 0, 0)
    end     = datetime(2100, 12, 31, 23, 59, 59)

    full    = end - start
    elapsed = ( (datetime.now() - start).total_seconds() / full.total_seconds() ) * 100

    on      = ( 15 * elapsed ) / 100
    off     = 15 - on
    bar_on  = u'\u2593' * int(on)
    bar_off = u'\u2591' * int(off)
    text    = bar_on + bar_off + ' ' + "%.4f" % elapsed + '%'

    if "TWEET" in os.environ:
        api = tweetpony.API(    consumer_key        = secrets.consumer_key,
                                consumer_secret     = secrets.consumer_secret,
                                access_token        = secrets.access_token_key,
                                access_token_secret = secrets.access_token_secret)
        api.update_status(text)

    return { 'message' : text }

