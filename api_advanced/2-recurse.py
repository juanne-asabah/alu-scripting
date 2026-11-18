#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot posts for a given subreddit.

    Returns None if the subreddit is not valid.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alu_student)"
    }
    params = {"after": after, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
