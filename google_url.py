# coding:utf-8

import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError
import random
import urllib
import types

def image_search(query, num):
    """Download full size images from Google image search.
        
        Don't print or republish images without permission.
        I used this to train a learning algorithm.
        """
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
        'v=1.0&q=' + query + '&start=%d'
   
    url_list = []

    for i in xrange(num) :
        r = requests.get(BASE_URL % i)

        if len(json.loads(r.text)['responseData']['results']) == 0:
            return False

        for image_info in json.loads(r.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            if url != "":
                url_list.append(url)

    print url_list
    return True

# Example use
#image_search('수지', 'myDirectory')
