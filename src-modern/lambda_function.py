#!/usr/bin/env python3

# LICENSE:
#   http://www.wtfpl.net/about/

"""
21st Century Progress Bar - Modern Python 3 Version

Tweets the progress of the 21st century (2001-2100) using Twitter API v2.
Designed for AWS Lambda with Python 3.11+ runtime.

Usage:
    Set environment variables:
    - CONSUMER_KEY
    - CONSUMER_SECRET
    - ACCESS_TOKEN_KEY
    - ACCESS_TOKEN_SECRET
    - TWEET (set to any value to actually post)
"""

from datetime import datetime, timezone
import os

import tweepy


def lambda_handler(event=None, context=None):
    """Calculate century progress and optionally tweet it."""
    
    # 21st century: Jan 1, 2001 00:00:00 UTC to Dec 31, 2100 23:59:59 UTC
    start = datetime(2001, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    end = datetime(2100, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)

    # Calculate elapsed percentage
    elapsed = ((now - start).total_seconds() / (end - start).total_seconds()) * 100

    # Build progress bar (15 blocks total)
    blocks_on = round(15 * elapsed / 100)
    blocks_off = 15 - blocks_on
    bar = '▓' * blocks_on + '░' * blocks_off
    text = f"{bar} {elapsed:.2f}%"

    # Tweet if TWEET environment variable is set
    if os.environ.get("TWEET"):
        client = tweepy.Client(
            consumer_key=os.environ["CONSUMER_KEY"],
            consumer_secret=os.environ["CONSUMER_SECRET"],
            access_token=os.environ["ACCESS_TOKEN_KEY"],
            access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
        )
        client.create_tweet(text=text)

    return {"message": text}


if __name__ == "__main__":
    # Local testing
    result = lambda_handler()
    print(result["message"])

