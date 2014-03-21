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

def image_search(query, path, num):
    """Download full size images from Google image search.
        
        Don't print or republish images without permission.
        I used this to train a learning algorithm.
        """
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
        'v=1.0&q=' + query + '&start=%d'
    
    index = random.randint(0, 20)
    r = requests.get(BASE_URL % 0)
    cnt = 0

    if len(json.loads(r.text)['responseData']['results']) == 0:
        return False

    for image_info in json.loads(r.text)['responseData']['results']:
        url = image_info['unescapedUrl']
        if (cnt >= index):
	    break
	cnt += 1

    if url == "":
        return False
    if not urllib.urlretrieve(url, "images/" + str(num) + ".jpg"):
        return False

    return True

# Example use
#go('수지', 'myDirectory')
