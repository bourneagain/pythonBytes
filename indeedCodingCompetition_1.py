from collections import Counter
from operator import itemgetter
import sys
def A(a):
	b=[]	
	c=[]
	for i in range(0,len(a)+1):
		 b.append(a[:i])
	for i in b:
		for j in i:
			c.append(j)
	x=Counter(c)
	a=sorted(x.items(), key=itemgetter(0))
	#print sorted(sorted(a, key=itemgetter(0)), key=itemgetter(1), reverse=True)
	print ''.join([i[0] for i in sorted(sorted(a, key=itemgetter(0)), key=itemgetter(1), reverse=True) ])
		
file,a=sys.argv
A(a)
