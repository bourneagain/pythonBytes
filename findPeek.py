def findPeek(a):
	res = findPeekH(a,0,len(a)-1)
	return res,a[res]

def findPeekH(a,start, end):
	print a[start:end+1],start,end
	if start==end:
		return start
	elif start+1 ==  end:
		if a[start] > a[end]:
			return start
		elif a[start] < a[end]:
			return end
	else: 
		m = (start + end) // 2 
		if a[m] > a[m - 1 ] and a[m] > a[m + 1]:
			return m
		elif a[m] > a[m - 1 ] and a[m] < a[m+1]:
			# lies on the right
			return findPeekH(a,m+1,end)
		else:
			return findPeekH(a,start,m-1)

A=[1,2,3,5,2,3]
print findPeek(A)
