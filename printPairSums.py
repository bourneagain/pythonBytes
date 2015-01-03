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
	return len(res),res

A=[-2,-1,0,3,5,6,7,9,13,14]
print printPairSums(A,6)