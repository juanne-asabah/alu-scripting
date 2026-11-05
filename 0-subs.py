#!/usr/bin/python3
"""
This module provides a function to query the Reddit API & return
the total number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total subscriber count for a subreddit, or 0 if invalid."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:subscriber-fetcher:v1.0 (by /u/Distinct-Park346)"
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
