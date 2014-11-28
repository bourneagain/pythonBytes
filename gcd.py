def gcd(x,y):
	while y!=0:
		(x,y)=(y,x%y)
	return x
def gcd_r(x,y):
	print x,":",y
	if y==0:
		return x
	else:
		return gcd_r(y,x%y) 

print gcd_r(10,5)
