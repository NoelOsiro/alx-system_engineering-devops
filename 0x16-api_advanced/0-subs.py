#!/usr/bin/python3
"""
00subs.py - Get no fo subscribers to a topic
"""
import requests

def number_of_subscribers(subreddit):
    """
    Get no fo subscribers to a topic
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomBot/1.0'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
