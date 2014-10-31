import sys
setIndex=[]
def bloomFilter(A):
	A=A.split(',')	
	A=[ int(x) for x in A]
	res={}
	val=""
	for i in A:
		res[i]=bloomHash(i)
	print res		

def bloomHash(K):
	global setIndex
	m=32
	haslist=[]
	for ha in range(1,4):
		biton=(((K**2+K**3)*ha)%32)
		setIndex.append(biton)
		haslist.append(biton);
	return haslist
	
def checkFalsePositive():
	print "ENTERED"
	global setIndex
	n=1;
	while True:
		a=bloomHash(1)
		print a 
		if len(set(a) & set(setIndex)) == len(set(a)):
			print set(a),set(setIndex) 
			break
		else:
			n=n+1
	
bloomFilter(sys.argv[1])
print setIndex
print set(setIndex)
print len(set(setIndex))

print "*****"
checkFalsePositive()



