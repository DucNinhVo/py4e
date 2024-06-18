import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving ', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved ',len(data), ' characters')

# print(tree) will print out the most current node
tree = ET.fromstring(data)

# findall('count') will just look for <count> in the current node (<commentinfo>)
# Using XPath selector findall('.//count') will search <count> in every child nodes from the current node
# its the same as 'comments/comment/count' 
counts = tree.findall('.//count')
print('Count: ',len(counts))

sum = 0
for count in counts:
    sum += int(count.text)

print('Sum: ', sum)

