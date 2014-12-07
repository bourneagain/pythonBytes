
def longestSum(A):
	currentSum=A[0]
	maxSum=A[0]
	print currentSum
	print maxSum
	print "BEFORE"
	for i in A[1:]:
		print "I " + str(i)
		print "CUR" + str(currentSum)
		currentSum=max(currentSum,currentSum+i)
		maxSum=max(maxSum,currentSum)
		print currentSum
		print maxSum
		print "___"
	return maxSum	

def max(a,b):
	print "INSIDE" 
	print a,b
	if  a > b : 
		print "returning " + str(a)
		return a
	else:
		return b


def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

A=[-3,-1,-1,-1]
print longestSum(A)
#print max_subarray(A)
