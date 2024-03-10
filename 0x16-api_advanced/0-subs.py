#!/usr/bin/python3
"""
Reddit Subreddit Subscriber Count Module

This module provides a function for querying the Reddit API and retrieving the
number of subs (total subs) for a specified subreddit.

Functions:
    - number_of_subs(subreddit): Queries the Reddit API and returns the
      number of subs for the given subreddit. If the subreddit is invalid,
      it returns 0.
"""

import base64
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subs for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subs for the subreddit. If the subreddit is invalid,
             it returns 0.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set the User-Agent and Authorization headers
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
            # Handle other errors
            else:
                return 0
        except Exception as e:
            return 0
