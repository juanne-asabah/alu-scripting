#!/usr/bin/python3
"""
This module provides a function that queries the Reddit API to retrieve
the total number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the total number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://reddit.com{subreddit}/about.json"
    headers = {"User-Agent": "linux:Parser:v1.0.0 (by u/Distinct-Park346)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except Exception:
        return 0
