#!/usr/bin/python3
""" RedditAPI Module that prints the titles of hot articles"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ queries the Reddit API and prints the titles of hot articles
    listed for a given subreddit recursively.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'\
          .format(subreddit, after)
    headers = {'User-Agent': 'Pizzosta'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        for article in articles:
            hot_list.append(article['data']['title'])

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        return None
