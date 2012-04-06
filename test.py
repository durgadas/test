from BeautifulSoup  import BeautifulSoup
import os
import sys
import urllib2
import urllib

url = urllib2.urlopen("http://www.tatadocomo.com/online-recharge.aspx")
print "page opened"
page = BeautifulSoup(url)
print ">>>>>>>>>>>>>>>>",page.title.text
text_box= page.findAll('input')
my_search = page.findAll('input',{'type':'text'})
print my_search
