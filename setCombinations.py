def sol(seta):
	res=[]
	count=2**len(seta)
	for i in range(count):
		newl=[]
		index=0
		j=i
		while j>0:
			if j&1 == 1:
				newl.append(seta[index])
			index+=1
			j=j>>1
		res.append(newl)
	return tuple(res)

A=('s','a','m')
print sol(A)