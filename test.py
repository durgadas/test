from BeautifulSoup  import BeautifulSoup
import os
import sys
import urllib2
import urllib

url = urllib2.urlopen("http://www.google.com")
print "page opened"
page = BeautifulSoup(url)
tables = page.findAll('table')
print "Tables are ",tables
