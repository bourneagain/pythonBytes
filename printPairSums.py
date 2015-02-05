import pprint
def printPairSums(array,s):
	res=[]
	b=0
	e=len(array)-1
	while b<e:
		su=array[b]+array[e]
#		print "LOOP",b,e,su
		if su == s:
			res.append(('index=>',b,e,'values=>',array[b],array[e]))
			b+=1
			e-=1
		else:
			if su > s:
				e-=1
			else:
				b+=1
	return "NumberOfPairs",len(res),res

def printPairsSumHash(array,s):
	""" 
	works for non sorted array as well
	"""
	res=[]
	h={}
	for index,i in enumerate(array):
		comp=s-i
		if comp in h:
			res.append(('index=>',index,h[comp],'values=>',i,comp))
		else:
			h[i]=index
	return "NumberOfPairs",len(res),res


A=[-2,-1,0,3,5,6,7,9,13,14]
print printPairSums(A,-1)
print printPairsSumHash(A,-1)
