def frac(n):
	#n=0.25
	a=[]
	count=10
	while True:
		t=n*2
		d=int(t/1)
		f=t%1
		a.append(d)
		if f!=0:
			n=f
			continue
		else:
			break
	print a

frac(0.625)
