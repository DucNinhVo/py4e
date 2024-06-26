import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving ', url)
data = urllib.request.urlopen(url,context=ctx).read()
print('Retrieved ',len(data), ' characters')

info = json.loads(data)['comments']
print('Count:', len(info))

sum = 0
for item in info:
    sum += item['count']

print(sum)
