def subArrayMax(A):
	sum=A[0];
	ans=A[0];
	for i in A:
		print i,
		sum+=i
		if sum > ans: 
			ans=sum
			print "incr ans " + str(ans)
		else:
			print "reset sum"
			sum=0
		print "ANS SO FAR IS " + str(ans)
	return ans


A=[1,-3,2,-5,7,6,-1,-4,11,-23]
A=[-2, -3, 4, -1, -2, 1, 5, -3]
print subArrayMax(A)
print A
				
