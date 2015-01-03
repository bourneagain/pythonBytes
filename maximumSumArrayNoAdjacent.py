"""
Maximum sum such that no two elements are adjacent
"""
def maxSum(a):
	inc=a[0]
	exc=0
	for i in a[1:]:
		temp=inc
		inc=exc+i
		exc=max(temp,exc)
	return max(inc,exc)


a=[5,  5, 10, 40, 50, 35]
print maxSum(a)