#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'My Bot 1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raises an exception for 4xx/5xx status codes
        data = response.json()
        return data['data']['subscribers']
    except (requests.RequestException, KeyError):
        return 0
