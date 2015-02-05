def set_combination(a):
	n = len(a)
	bits  = 1<<n
	res = []
	for i in range(bits):
		temp = []
		one_list = one_index(i)
		for i in one_list:
			temp.append(a[i])
		res.append(temp)
	return res

def one_index(a):
	a = int(a)
	count=[]
	ci = 0
	while a > 0:
		if a&1:
			count.append(ci)
		a=a>>1
		ci+=1
	return count

print set_combination(('s','a','m'))
#print one_index(10)
