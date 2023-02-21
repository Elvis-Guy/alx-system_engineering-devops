#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after='', word_dict={}):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        print('Invalid subreddit')
        return
    data = response.json().get('data')
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title')
        title_words = [word.lower() for word in title.split()]
        for word in word_list:
            if word.lower() in title_words:
                word_dict[word.lower()] = word_dict.get(word.lower(), 0) + title_words.count(word.lower())
    after = data.get('after')
    if after is None:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print('{}: {}'.format(word, count))
        return
    count_words(subreddit, word_list, after, word_dict)
