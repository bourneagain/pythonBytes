def nestedSum(a,depth):
	s=0
	for i in a:
		if isinstance(i,list):
			s+=nestedSum(i,depth+1)
		else:
			s+=i*depth
	return s


a=[[1,1],2,[1,1]]
b=[1,[4,[6]]]
print nestedSum(b,1)



