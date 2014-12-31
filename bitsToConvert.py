def bit_req(A,B):
	"""
	Bits required to convert int A to int B
	"""
	c=A^B
	return countOnes(c)

def countOnes(c):
	count=0
	if c == 1:
		return 1
	while(c>=1):
		b=c%2
		if b == 1:
			count+=1
		c=c//2
	return count

print bit_req(4,7)	
