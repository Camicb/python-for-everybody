#Scraping Numbers from HTML using BeautifulSoup In this assignment you will
#write a Python program similar to http://www.py4e.com/code3/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers
#in the file.

#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_884363.html (Sum ends
#with 10)
#You do not need to save these files to your folder since your program will
#read the data directly from the URL. Note: Each student will have a distinct
#data url for the assignment - so only use your own data url for analysis.
#You are to find all the <span> tags in the file and pull out the numbers
#from the tag and sum the numbers.
#You need to adjust this code to look for span tags and pull out the text
#content of the span tag, convert them to integers and add them up to complete
#the assignment.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')

lista=list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    content=tag.contents[0]
    num=int(content)
    lista.append(num)
    
print(sum(lista))

