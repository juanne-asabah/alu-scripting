#!/usr/bin/python3
"""Recursively queries the Reddit API and returns all hot article titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit."""
    url = f"https://reddit.com{subreddit}/hot.json"
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after is None:
        return hot_list

    return recurse(subreddit, hot_list, next_after)
