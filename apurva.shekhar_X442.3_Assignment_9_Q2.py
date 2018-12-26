# Write a script that will list and count all of the images in a given HTML web
# page/file. You can assume that:
#    Each image file is enclosed with the tag <img and ends with >
#    The HTML page/file is syntactically correct.

import urllib.request
import ssl
import re

# Set up the context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_image():
    url = input('Enter URL here: ')
    page  = urllib.request.urlopen(url, context=ctx).read()
    compiled_image = re.compile(rb'''<img.*>''', re.IGNORECASE)
    image_tags = compiled_image.findall(page)
    count = len(image_tags)
    print('Total Count :', count)

get_image()
