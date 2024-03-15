#!/usr/bin/python3

"""
This module defines a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print("Invalid subreddit.")
        return None
    
    data = response.json()
    children = data['data']['children']
    
    for i in range(10):
        post = children[i]['data']
        print(f"{i+1}. {post['title']}")
