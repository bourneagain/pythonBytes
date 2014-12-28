import  time
def bst(A,n):
	start=0
	end=len(A)-1
	while(start<=end):
		time.sleep(1)
		print start,end
		mid = start + (end-start)//2 
		if n == A[mid]:
			return mid 
		elif n < A[mid]:
			end = mid - 1
		elif n > A[mid]:
			start = mid + 1
	return -1

print bst([2,3,5,10],20)
A=[22]
print bst(A,2)
