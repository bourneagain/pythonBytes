def intersectionOfSortedArrays(a,b):
	"""
	less than o(m+n) complexity
	"""
	ia=0
	ib=0
	op=[]
	while ia<len(a) and ib<len(b):
		if a[ia] < b[ib]:
			ia+=1
		elif a[ia] > b[ib]:
			ib+=1
		else:
			op.append(a[ia])
			ia+=1
	return op

a=[1,3,4,5,6,7,8,9]
b=[2,3,5,8,]
print intersectionOfSortedArrays(a,b)





