#!/usr/bin/python3
"""Script that returns top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Function that prints top 10 posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    data = response.json()

    if response.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
