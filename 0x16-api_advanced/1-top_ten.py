#!/usr/bin/python3
""" RedditAPI Module that prints the titles of the first 10 hot """

import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Pizzosta'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']['children']
        for post in hot_posts:
            print(post['data']['title'])
    else:
        print(None)
