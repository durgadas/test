from BeautifulSoup  import BeautifulSoup
import os
import sys
import urllib2
import urllib

#url = urllib2.urlopen("http://www.tatadocomo.com/online-recharge.aspx")
#print "page opened"
#page = BeautifulSoup(url)
#print ">>>>>>>>>>>>>>>>",page.title.text
#text_box= page.findAll('input')
#my_search = page.findAll('input',{'type':'text'})
#print my_search
class my_class:
	def __init__(self):
		print "I am called automatically"
		self.data =[]
	i  = 12345
	def show(self,n):
		print n

x = my_class()
x.show(200)
