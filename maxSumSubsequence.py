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


def max_sum(a):
	"""
	returns start and end position of the array also
	"""
	start=0
	end=0
	s=0
	max_s=0
	for index, i in enumerate(a):
		s+=i
		if s < 0:
			s=0
			start = index+1
		elif s > max_s:
			end=index
			max_s=s
	return max_s,(start,end),(a[start:end+1])

a=[-2,1,-3,4,-1,2,1,-5,4]
print max_sum(a)

A=[5,-9,6,-2,3]
B=[-2,1,-3,4,-1,2,1,-5,4]
print maxSumSubsequence(A)
print maxSumSubsequence(B)