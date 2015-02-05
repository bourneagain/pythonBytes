def m(a):
	c=0
	m=a[0]
	for i in a:
		if i == m:
			c+=1
		else:
			c-=1
		if c==0:
				m=i
				c=1
	c=0
	for i in a:
		if i == m:
			c+=1
	if c>=len(a)//2+1:
		return m
	else:
		return None

print m([1,2,3,2,5,2,6,2])
