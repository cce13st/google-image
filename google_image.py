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

def go(query, path, num):
    """Download full size images from Google image search.
        
        Don't print or republish images without permission.
        I used this to train a learning algorithm.
        """
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
        'v=1.0&q=' + query + '&start=%d'
    
 #   BASE_PATH = os.path.join(path, query)
    
 #   if not os.path.exists(BASE_PATH):
 #       os.makedirs(BASE_PATH)
    
    index = random.randint(0, 3)
    r = requests.get(BASE_URL % 0)
    cnt = 0

    if len(json.loads(r.text)['responseData']['results']) == 0:
        return False

    for image_info in json.loads(r.text)['responseData']['results']:
        url = image_info['unescapedUrl']
        if (cnt >= index):
	    break
	cnt += 1

    if not urllib.urlretrieve(url, "images/" + str(num) + ".jpg"):
        return False

    return True
    '''
	    try:
                image_r = requests.get(url)
            except ConnectionError, e:
                print 'could not download %s' % url
                continue
            
            # Remove file-system path characters from name.
            title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')
            
            file = open(os.path.join(BASE_PATH, '%s.jpg') % title, 'w')
            try:
                Image.open(StringIO(image_r.content)).save(file, 'JPEG')
            except IOError, e:
                # Throw away some gifs...blegh.
                print 'could not save %s' % url
                continue
            finally:
                file.close()
        
        print start
        start += 4 # 4 images per page.
        # Be nice to Google and they'll be nice back :)
        time.sleep(1.5)
    '''

# Example use
#go('수지', 'myDirectory')
