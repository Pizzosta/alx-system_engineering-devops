#!/usr/bin/python3
""" RedditAPI Module"""

import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Pizzosta'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        total_subscribers = data['data']['subscribers']
        return total_subscribers
    else:
        return 0
