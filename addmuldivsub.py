def mul(a,b):
	neg=False
	if a<0 and b>0:
		a=invert(a)
		neg=True
	if a>0 and b<0:
		b=invert(b)
		neg=True
	if a<0 and b<0:
		a=invert(a)
		b=invert(b)
	res=0
	while b>0:
		res+=a
		b-=1
	return invert(res) if neg else res

def invert(a):
	return ~a+1

print mul(0,-1)

