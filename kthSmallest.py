def kthSmall(a,b,k):
	count=1
	n=len(a)
	m=len(b)
	if n == 0 or m == 0:
		return -1
	if n+m < k:
		return -1
	ia=0
	ib=0
	kelm=-1
	while count <= k:
		if ia==n:
			kelm=b[ib]
			ib+=1
		elif ib==n:
			kelm=a[ia]
			ia+=1
		elif a[ia] <= b[ib]:
			kelm=a[ia]			
			ia+=1
		else:
			kelm=b[ib]
			ib+=1			
		#print kelm
		count+=1
	return kelm

a=[-4,1]
b=[-1,13,24,45]
print kthSmall(a,b,3)


