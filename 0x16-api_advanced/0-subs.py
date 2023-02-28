#!/usr/bin/python3
"""Function to GET number of subscribers for a given subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """Use GET request to find number of subsceibers to "subreddit'"""
    r = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
            patams={"raw_json": 1},
            headers={"User-Agent": "Timothy from ALX"},
            allow_redirects=False)

    try:
        r.raise_from_status()
    except:
        return 0
    else:
        num_subscribers = r.json().get('data').get('subscribers')
        if num_subscribers is None:
            return 0
        return num_subscribers
