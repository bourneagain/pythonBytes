def firstMissingPositive( A):
	head,tail=0,len(A)-1
# reorder A to ensure the first head elements are positive number
	while head<=tail:
		if A[head]<=0 and A[tail]>0:
			A[head],A[tail]=A[tail],A[head]
			head,tail=head+1,tail-1
		elif A[head]>0:
			head+=1
		elif A[tail]<=0:
			tail-=1; 
		print A,head
	for i in range(head):
		if abs(A[i]) <= head:
			A[abs(A[i])-1] = -abs(A[abs(A[i])-1])
			print A

print firstMissingPositive([1,2,3,4,5,40,7,8,9,11,12])