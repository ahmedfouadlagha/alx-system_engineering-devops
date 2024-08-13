#!/usr/bin/python3
"""
Retrieves the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'your_user_agent'}  # Replace with your custom User-Agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for error HTTP statuses

        data = response.json()
        return data['data']['subscribers']

    except (requests.exceptions.RequestException, KeyError):
        # Handle potential errors like connection issues, invalid JSON, or missing key
        return 0
