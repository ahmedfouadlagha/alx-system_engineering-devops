#!/usr/bin/python3
"""A script that gets the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Function that requests the number of subscribers for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers if the subreddit exists, 0 otherwise.
    """
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    USER_AGENT = "com.holbertonschool.myredditscript:0.0.1 (by /u/dmaring)"
    headers = {'User-Agent': USER_AGENT}
    
    # Making the request to the Reddit API
    r = requests.get(URL, headers=headers, allow_redirects=False)
    
    # Check if the request was successful and not redirected
    if r.status_code != 200:
        return 0
    
    # Parse the response as JSON
    try:
        r = r.json()
        return r['data']['subscribers']
    except (KeyError, ValueError):
        return 0
