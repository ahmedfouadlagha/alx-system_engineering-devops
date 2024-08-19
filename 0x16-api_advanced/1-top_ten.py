#!/usr/bin/python3
"""Script that returns top 10 hot posts of a subreddit"""
import requests

def top_ten(subreddit):
    """Function that prints top 10 posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(url, headers={'User-Agent': 'app/1.0'}, allow_redirects=False)
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data['data']['children']
                for post in posts:
                    print(post['data']['title'])
            except ValueError:
                # JSON decoding failed, possibly because of an unexpected response
                print(None)
        else:
            # Handle cases where the subreddit does not exist or is invalid
            print(None)
    
    except requests.RequestException:
        # Handle network-related errors
        print(None)
