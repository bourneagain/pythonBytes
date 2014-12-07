result=[]
def magic(A,l,h):
	global result
	if h<l  or l < 0 or h > len(A):
		return result
 	mid=l+(h-l)/2

	if A[mid] == mid:
		print A[mid]
		result.append(mid)
		return magic(A,mid+1,h)
	if A[mid] < mid:
		return magic(A,mid+1,h)
	if A[mid] > mid:
		return magic(A,l,mid-1)

A=[-5,-2,1,3,4,7,8]
print magic(A,0,len(A))