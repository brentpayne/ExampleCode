#!python
'''
some example beautiful soap code to parse imperect xml style documents (such as html)

most code comes from 
http://www.crummy.com/software/BeautifulSoup/documentation.html#Parsing%20HTML

there is so much in BeautifulSoap the website is the best place to find what you need.  I'll add more in here as I use it more.  check out the Design Out Of Reach module.
'''

#print pretty
from BeautifulSoup import BeautifulSoup
html = "<html><p>Para 1<p>Para 2<blockquote>Quote 1<blockquote>Quote 2"
soup = BeautifulSoup(html)
print soup.prettify()

#grep
from BeautifulSoup import BeautifulSoup
import re
hello = "Hello! <!--I've got to be nice to get what I want.-->"
commentSoup = BeautifulSoup(hello)
comment = commentSoup.find(text=re.compile("nice"))

#

if __name__ == '__main__':
  print 'This file is example code, may not even compile much less run'
