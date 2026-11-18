#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of the given keywords (case-insensitive).
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints a sorted count of keywords found in a subreddit's hot titles.

    Words are matched case-insensitively and must be delimited by spaces
    (so "java." does not count as "java"). Duplicates in word_list add up.
    Prints nothing if the subreddit is invalid or no keywords match.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alu_student)"
    }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    wanted = set(word.lower() for word in word_list)
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in wanted:
                counts[token] = counts.get(token, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    # Last page reached: apply duplicate multipliers, sort and print
    multiplier = {}
    for word in word_list:
        multiplier[word.lower()] = multiplier.get(word.lower(), 0) + 1

    results = [(word, total * multiplier[word])
               for word, total in counts.items() if total > 0]
    for word, total in sorted(results, key=lambda item: (-item[1], item[0])):
        print("{}: {}".format(word, total))
