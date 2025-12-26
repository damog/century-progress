#!/usr/bin/env python

# LICENSE:
#   http://www.wtfpl.net/about/

from datetime import datetime, timezone
import os

import tweetpony
import secrets


def lambda_handler(event=None, context=None):
    start = datetime(2001, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    end = datetime(2100, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)

    elapsed = ((now - start).total_seconds() / (end - start).total_seconds()) * 100

    blocks_on = round(15 * elapsed / 100)
    blocks_off = 15 - blocks_on
    bar_on = '\u2593' * blocks_on
    bar_off = '\u2591' * blocks_off
    text = f"{bar_on}{bar_off} {elapsed:.2f}%"

    if "TWEET" in os.environ:
        api = tweetpony.API(
            consumer_key=secrets.consumer_key,
            consumer_secret=secrets.consumer_secret,
            access_token=secrets.access_token_key,
            access_token_secret=secrets.access_token_secret
        )
        api.update_status(text)

    return {'message': text}

