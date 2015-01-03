def addwithoutaddition(a,b):
	if b == 0:
		return a
	s=a^b
	c=(a&b)<<1
	return addwithoutaddition(s,c)

print addwithoutaddition(1,2)