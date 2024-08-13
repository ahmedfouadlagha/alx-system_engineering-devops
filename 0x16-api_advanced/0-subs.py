#!/usr/bin/python3
""" Script that returns no. of subscribers of a subreddit """
import requests


def number_of_subscribers(subreddit):
    """Function that returns no. of subs of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-Agent': 'selBot/1.0'})
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
