#!/usr/bin/python3
"""Script that returns top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Function that prints top 10 posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(
            url, headers={'User-Agent': 'app/1.0'}, allow_redirects=False
        )

        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data', {}).get('children', [])

                if posts:
                    for post in posts:
                        print(post['data'].get('title'))
                else:
                    print(None)
            except ValueError:
                print(None)
        else:
            print(None)

    except requests.RequestException:
        print(None)
