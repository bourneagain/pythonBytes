def findMinMax(a,b):
	A=flip(sign(a-b))
	B=flip(A)
	return a*A+b*B

def sign(a):
	return a>>63 & 0x1
def flip(a):
	return 1^a

print findMinMax(1,-1)