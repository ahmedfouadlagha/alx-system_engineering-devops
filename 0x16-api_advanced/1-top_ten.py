#!/usr/bin/python3

"""
This module defines a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""
import requests

def top_ten(subreddit):
  """Fetches and prints titles of the top 10 hot posts for a subreddit.

  Args:
      subreddit: The name of the subreddit to search (string).

  Prints:
      Titles of the top 10 hot posts (or None if subreddit is invalid).
  """

  # Reddit API endpoint for hot posts
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

  # Disable following redirects to avoid irrelevant results
  response = requests.get(url, allow_redirects=False)

  # Check for successful response (status code 200)
  if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    
    # Check if data contains listings
    if 'data' in data and 'children' in data['data']:
      # Extract titles of top 10 posts
      for post in data['data']['children'][:10]:
        print(post['data']['title'])
    else:
      print("Subreddit has no posts or invalid response format.")
  else:
    # Print message for invalid subreddit or other errors
    print(f"Error: {response.status_code} - Subreddit might not exist.")

# Example usage (assuming 1-main.py is in the same directory)
if __name__ == "__main__":
  import sys
  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
  else:
    top_ten(sys.argv[1])
