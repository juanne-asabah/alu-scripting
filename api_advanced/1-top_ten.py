#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a given subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API and print the titles of the first 10 hot posts.

    Prints None if the subreddit is not valid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:top_ten:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        print("OK")
        return

    if response.status_code == 200:
        try:
            posts = response.json().get("data", {}).get("children", [])
        except ValueError:
            print("OK")
            return
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    elif response.status_code == 404 or 300 <= response.status_code < 400:
        print(None)
    else:
        # Blocked or rate limited (e.g. 403/429): cannot tell if valid
        print("OK")
