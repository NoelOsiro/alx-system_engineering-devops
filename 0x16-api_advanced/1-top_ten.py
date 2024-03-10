#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import base64
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    code = "Rb1PJ7q615K2oGNI871S4w:jaUSqXlK0P4nFdEGleLCoe9SpgrF2w"
    auth_header_value = base64.b64encode(
            code.encode("utf-8")).decode("utf-8")
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        'User-Agent': 'alx-pass/1.0',
        'Authorization': f'Basic {auth_header_value}'
        }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
