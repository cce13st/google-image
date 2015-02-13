# coding:utf-8
import json
import requests
import random
import urllib
import os

def downloadImage(url_list, directory):
    '''
    "image_search" finds number of images from google image search,
    and store it to target directory

    Parameters
        url_list : list of string url
        directory : directory for store images

    Return value
        return number of successfully downloaded images
    '''

    cnt = 0

    if len(url_list) == 0:
        print "url_list is empty!"
        return 0

    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in url_list:
        if url == "":
            continue
        if not urllib.urlretrieve(url, directory + "/" + str(cnt) + ".jpg"):
            continue
        cnt += 1

    return cnt

def searchImageUrl(query, num):
    '''
    "searchImageUrl" finds number of images from google image search,
    and return found images url

    Parameters
        query : query string for searching
        num : # of images to find

    Return value
        return a tuple (# of images found, num)
    '''

    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
        'v=1.0&q=' + query + '&start=%d'
   
    url_list = []

    for i in xrange(num) :
        r = requests.get(BASE_URL % i)

        if len(json.loads(r.text)['responseData']['results']) == 0:
            return []

        for image_info in json.loads(r.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            if url != "":
                url_list.append(url)

    return url_list

# Example usage
# searchImageUrl('California', 10)