#!/usr/bin/python3
"""Recursively counts and sorts keyword occurrences in hot Reddit titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None, multipliers=None):
    """Queries Reddit API recursively and prints sorted keyword counts."""
    if counts is None:
        counts = {}
        multipliers = {}
        for word in word_list:
            lower_w = word.lower()
            counts[lower_w] = 0
            multipliers[lower_w] = multipliers.get(lower_w, 0) + 1

    url = f"https://reddit.com{subreddit}/hot.json"
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        title_words = post.get("data", {}).get("title", "").lower().split()
        for token in title_words:
            if token in counts:
                counts[token] += 1

    next_after = data.get("after")
    if next_after is not None:
        return count_words(subreddit, word_list, next_after, counts, multipliers)

    final_counts = {
        word: count * multipliers[word]
        for word, count in counts.items()
        if count > 0
    }

    sorted_words = sorted(
        final_counts.items(), key=lambda item: (-item[1], item[0])
    )
    for word, total in sorted_words:
        print(f"{word}: {total}")
