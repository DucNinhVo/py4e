# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
tags = []

# Repeat the process 'count' times
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    print('Retrieving:',url)
    tags = soup('a')
    
    #Find the link at position 'pos and follow that link
    url = tags[pos - 1].get('href', None)
      
# print out the last name 
print('Retrieving:',url)
print(tags[pos - 1].contents[0])
    