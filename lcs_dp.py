def lcs(s1, s2):
	lcs_dp={}
	l=[]
	result=0
	for i in range(len(s1)+1):
		for j in range(len(s2)+1):
			if i==0 or j==0:
				lcs_dp[i,j]=0
			elif s1[i-1] == s2[j-1]:
				lcs_dp[i,j]=lcs_dp[i-1,j-1]+1
				result=max(result,lcs_dp[i,j])
				l.append(s1[i-1])
			else:
				lcs_dp[i,j]=0

	return result,l

s1="sama"
s2="kumarasamaraj"

print lcs(s1,s2)
