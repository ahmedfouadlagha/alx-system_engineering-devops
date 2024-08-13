#!/usr/bin/python3
"""
Script that returns the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurred.
    """

    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'selBot/1.0'}

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        return data['data']['subscribers']

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for subreddit '{subreddit}': {e}")
        return 0

# Example usage (assuming you have a way to get the subreddit name)
subreddit_name = "learnpython"  # Replace with the desired subreddit
subscribers = number_of_subscribers(subreddit_name)
print(f"Number of subscribers for r/{subreddit_name}: {subscribers}")
