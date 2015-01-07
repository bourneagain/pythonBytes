def re(filename):
	"""
	sample code to read byte by byte from a file and reverse 
	"""
	with open(filename,'r+') as f:
		seekposition=0
		while( f.read(8) != ''):
			print "done",
			f.seek(seekposition)
			a=f.read(8)
			print a,
			print f.tell(),
			f.seek(seekposition)
			print f.tell()
			f.write(a[::-1])
			seekposition+=8

re('/Users/sam/pythonBytes/a')
