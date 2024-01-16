#!/usr/bin/python3
"""Function to print top 10 posts on a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 top posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by NoelOsiro)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        # Parse the JSON response to get post information
        data = response.json()

        # Check if the 'data' key and 'children' key exist in the response
        if 'data' in data and 'children' in data['data']:
            # Extract and print the titles of the first 10 posts
            for i, post in enumerate(data['data']['children'][:10]):
                print(f"{post['data']['title']}")
        else:
            # Print None if the required keys are not present
            print("None")
    else:
        # Print None if the request was not successful
        print("None")
