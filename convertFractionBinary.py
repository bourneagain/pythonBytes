def con(n):
	#0.625
	res=[]
	res.append('.')
	if n <=0 or n >=1:
		return -1
	count=1;
	n=n%1
	while count <= 32:
		t=n*2
		bit=t//1
		if bit == 1:
			res.append('1')
		if bit == 0:
			res.append('0')
		frac=t%1
		if frac == 0:
			return ''.join(res)
		else:
			n=frac

print con(.6875)
print con(.1)
				
		
				
