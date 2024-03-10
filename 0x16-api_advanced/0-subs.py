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
    code = "Rb1PJ7q615K2oGNI871S4w:jaUSqXlK0P4nFdEGleLCoe9SpgrF2w"
    try:
        auth_header_value = base64.b64encode(
            code.encode("utf-8")).decode("utf-8")
        req = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={
                'User-Agent': 'alx-pass/1.0',
                'Authorization': f'Basic {auth_header_value}'
            }
        )
        req.raise_for_status()
        if req.status_code == 200:
            return req.json().get("data").get("subscribers")
        else:
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
