import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')#fix the html mess

#Retrieve all of the anchor tags
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))

#Enter: http://www.dr-chuck.com/page1.htm
#respuesta: http://www.dr-chuck.com/page2.htm
