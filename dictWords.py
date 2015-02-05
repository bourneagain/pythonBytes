
import re,sys

a=[1,2,3,4,5,6]
print filter(lambda x: x%2 == 0,a)

sys.exit()

def check_if_present(a,b):
	"""
	to check if b contains only letters from a, only once
	a='abcdei'
	b='is'
	"""
	_len=0
	for i in a:
		if b.count(i) > a.count(i):
			return -1
		if b.count(i)== a.count(i):
			_len+=1
		#print i,b.count(i)
	if _len == len(b):
		return 1
	else:
		return 0

wordstring='aabase'
a=['Abaris','abarthrosis','abarticular','abarticulation','abas','abase','as','is']
regex='(^[a-zA-z]{3,}$)'
for i in a:
	a=re.match(regex,i)
	if a:
		 print i,check_if_present(wordstring,a.groups()[0])





#print check_if_present(wordstring,'is')
