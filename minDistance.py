def prod(a):
	lp=[1]*len(a)
	rp=[1]*len(a)
	lp[0] = 1
	for i in range(1,len(a)):
		lp[i] = lp[i-1]*a[i-1]
