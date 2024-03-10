#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests
import base64


def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'alx-pass/1.0',
        'Authorization': f'Basic {base64.b64encode(
            b"Rb1PJ7q615K2oGNI871S4w:jaUSqXlK0P4nFdEGleLCoe9SpgrF2w")
            .decode("utf-8")}'
    }
    # Create a session to reuse connections
    with requests.Session() as session:
        session.headers.update(headers)
        try:
            # Make a GET request to the Reddit API
            response = session.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Extract and return the number of subscribers
                return data['data']['subscribers']
            # Check if the subreddit is invalid (status code 404)
            elif response.status_code == 404:
                return 0
            else:
                return 0
        # Handle potential exceptions (e.g., network issues)
        except Exception as e:
            return 0
