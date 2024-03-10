#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import base64
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'alx-pass/1.0',
        'Authorization': f'Basic {base64.b64encode(
            b"Rb1PJ7q615K2oGNI871S4w:jaUSqXlK0P4nFdEGleLCoe9SpgrF2w")
            .decode("utf-8")}'
    }
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
