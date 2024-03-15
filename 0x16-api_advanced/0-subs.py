#!/usr/bin/python3
"""
This module defines a function to retrieve the number
of subscribers for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
