
#1998,2001,2004,2007,2010,2013,


import sys
setIndex=[]
def bloomFilter(A):
	A=A.split(',')	
	A=[ int(x) for x in A]
	res={}
	val=""
	for i in A:
		res[i]=bloomHash(i,0)
	print res		

def bloomHash(K,n):
	print "K"+str(K)
	global setIndex
	m=32
	haslist=[]
	for ha in range(1,4):
		biton=(((K**2+K**3)*ha)%32)
		print "biton is " + str(biton)
		if n==0: 
			setIndex.append(biton)
		haslist.append(biton);
	print haslist
	return haslist
	
def checkFalsePositive():
	print "ENTERED"
	global setIndex
	n=1987
	while True:
		a=bloomHash(n,1)
		print a
		if len(set(a) & set(setIndex)) == len(set(a)):
			print set(a),set(setIndex) 
			print n 
			break
		else:
			n=n+1
	
bloomFilter(sys.argv[1])
print setIndex
print set(setIndex)
print len(set(setIndex))

print "*****"
checkFalsePositive()



