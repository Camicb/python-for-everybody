#The program will prompt for a URL, read the JSON data from that
#URL using urllib and then parse and extract the comment counts
#from the JSON data, compute the sum of the numbers in the file.



import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' http://py4e-data.dr-chuck.net/comments_884366.json'
uh = urllib.request.urlopen(url, context=ctx)
link = uh.read()

data = json.loads(link)
total = 0
for item in data["comments"]:
    #print(item["count"])
    num = int(item["count"])
    total = total + num
print(total)
