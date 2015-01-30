def lcs_recursive(a,b):
	if not a or not b:
		return 0
	if a[-1] == b[-1]:
		return 1 + lcs_recursive(a[:-1],b[:-1])		
	else:
		return max(lcs_recursive(a,b[:-1]) , lcs_recursive(a[:-1],b) )



def lcs_dp(a,b):
	lcs_dp={}
	for i in range(len(a)+1):
		for j in range(len(b)+1):
			if i == 0 or j == 0:
				lcs_dp[i,j] = 0
				# lcs_dp stores the max length of common substring which ends at i-1,j-1 for a and b
			elif a[i-1] == b[j-1]:
				lcs_dp[i,j] = 1 + lcs_dp[i-1,j-1]
			else:
				lcs_dp[i,j] = max(lcs_dp[i,j-1],lcs_dp[i-1,j])
	# return lcs_dp[len(a),len(b)]

	# to print 
	i = len(a)
	j = len(b)
	res=[None]*lcs_dp[i,j]
	index = lcs_dp[i,j]-1
	while i>0 and j>0:
		if a[i-1] == b[j-1]:
			res[index] = a[i-1]
			index-=1
			i-=1
			j-=1
		else:
			if lcs_dp[i-1,j] > lcs_dp[i,j-1]:
				i-=1
			else:
				j-=1
	return res


	


print lcs_recursive('ABCDGH','AEDFHR')
print lcs_dp('xmjyauz','mzjawxu')

