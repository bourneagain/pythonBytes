def sortStack(st):
	rst = []
	while st:
		temp = st.pop()
		while rst and temp < rst[-1]:
			st.append(rst.pop())
		rst.append(temp)
	return rst

a=[15,1,4,6,12]
print sortStack(a)