def maxSumSubsequence(a):
	_sum=0
	_max_sum=0
	for i in a:
		if _sum+i > 0:
			_sum=_sum+i
		else:
			_sum=0
		if _sum > _max_sum:
			_max_sum=_sum
		#print "RESU",i,"|",	_sum,_max_sum
	return a,_max_sum

A=[5,-9,6,-2,3]
B=[-2,1,-3,4,-1,2,1,-5,4]
print maxSumSubsequence(A)
print maxSumSubsequence(B)