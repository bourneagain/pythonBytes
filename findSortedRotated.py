def findEle(A,first,last,n):
	middle=first+(last-first)/2

	if first > last:
		return -1

	if n == A[first]:
		return first
	if n == A[last]:
		return last

	if n == A[middle]:
		return middle

	if A[middle] > A[first]:
		if n > A[first] and n < A[middle]:
			return findEle(A,0,middle-1,n)
		else:
			return findEle(A,middle+1,last,n)
	elif A[middle] < A[first]:
		if n > A[middle] and n < A[last]:
			return findEle(A,middle+1,last,n)
		else:
			findEle(A,0,middle-1,n)
	elif A[middle] == A[first]:
		if n > A[middle]:
			return findEle(A,middle+1,last,n)

A=[1,1,1,1,1,1,2]
#print bfind(A,5)
print findEle(A,0,len(A)-1,2)