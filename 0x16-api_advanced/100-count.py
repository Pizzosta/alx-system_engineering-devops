#!/usr/bin/python3
"""
RedditAPI Module that prints the titles of hot articles
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count
as javascript, but java should not)
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Queries the Reddit API and prints the titles of hot articles
    and prints a sorted count of given keywords
    for a given subreddit recursively.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Pizzosta'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        if count_dict is None:
            count_dict = {}

        for article in articles:
            title = article['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    if word in count_dict:
                        count_dict[word] += 1
                    else:
                        count_dict[word] = 1

        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after=after,
                               count_dict=count_dict)
        else:
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_counts:
                print('{}: {}'.format(word.lower(), count))
    else:
        return None
