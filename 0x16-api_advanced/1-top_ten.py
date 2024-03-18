#!/usr/bin/python3
""" module 1-top_ten.py """
import requests
from operator import itemgetter

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/top.json?limit=10'
    headers = {'User-Agent': 'my-reddit-api-client'}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if data['kind'] == 't5':
        top_posts = data['data']['children']
        top_posts = sorted(top_posts, key=lambda x: x['data']['score'], reverse=True)
        top_posts = [{'title': post['data']['title'], 'score': post['data']['score']} for post in top_posts]
        return top_posts
    else:
        return []
