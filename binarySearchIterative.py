def bst(A,k):
	start=0
	end=len(A)-1
	while(start<=end):
		mid=start+(end-start)/2
		#print start,mid,end
		if A[mid]==k:
			return mid
		elif A[mid]<k:
			#print "less"
			start=mid+1
		elif A[mid]>k:
			#print "more"
			end=mid-1

	return -1 

A=[1]
print bst(A,1)
		






