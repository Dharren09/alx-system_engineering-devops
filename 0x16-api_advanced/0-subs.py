#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of 
subscribers (not active users, total subscribers) for a given subreddit.
 If an invalid subreddit is given, the function should return 0.
 """
import requests


def number_of_subscribers(subreddit):
    # Make a GET request to the subreddit's about page
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit) 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
