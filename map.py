import sys
try:
	list = map(int,sys.argv[1:])   
except ValueError:
	print "input integers"
print list
