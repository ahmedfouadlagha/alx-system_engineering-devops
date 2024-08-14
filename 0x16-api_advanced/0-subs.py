#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Custom User-Agent for subreddit queries'}
    # Define the API URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If subreddit is invalid, return 0
            return 0
    except Exception:
        # In case of any exceptions, return 0
        return 0
