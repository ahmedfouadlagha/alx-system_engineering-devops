#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
        
    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    try:
        req = requests.get(url, headers=headers, params=params, timeout=10)
        
        # Check if the response is JSON
        if req.headers.get('Content-Type') != 'application/json':
            print(None)
            return

        req.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

        data = req.json().get("data", {}).get("children", [])
        if not data:
            print(None)
            return

        for item in data:
            title = item.get("data", {}).get("title")
            if title:
                print(title)
            else:
                print(None)
    except requests.exceptions.RequestException as e:
        print(None)
