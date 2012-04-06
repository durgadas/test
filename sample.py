import fileinput
import re
import glob
import socket
str = "welcome to the world of python"
m  = re.findall("to",str)
if m:
	print "This is happened"
	print m

s = re.sub("of","",'Welcome to the world of python')
print s

pattern = re.compile('o')
print pattern.match('dog')
print pattern.match('dog',1)

d = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcoln Reynolds")
print d.group('first_name')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print s
