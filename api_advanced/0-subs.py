#!/usr/bin/python3
"""
This module writes a function that queries an API & returns
the number of subscribers for a given subreddit. An invalid
subreddit returns 0.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit.

    Returns 0 if the subreddit is invalid.
    """

    clean_name = subreddit.strip("/").replace("r/", "")

    # https://www.reddit.com/r/pics/about.json
    url = f"https://www.reddit.com/r/{clean_name}/about.json"
    # headers = {"User-Agent": "linux:suscriber-count:v7.7  (by u/Distinct-Park346)"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"}

    print(f"INFO: sending request to {url}", file=sys.stderr)


    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        print(f"INFO: Got a response of status code {response.status_code}", file=sys.stderr)


        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except Exception:
        return 0
