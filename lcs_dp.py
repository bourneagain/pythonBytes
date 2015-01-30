	
# def lcs(s1, s2):
# 	lcs_dp={}
# 	l=[]
# 	result=0
# 	for i in range(len(s1)+1):
# 		for j in range(len(s2)+1):
# 			if i==0 or j==0:
# 				lcs_dp[i,j]=0
# 			elif s1[i-1] == s2[j-1]:
# 				lcs_dp[i,j]=lcs_dp[i-1,j-1]+1
# 			else:
# 				lcs_dp[i,j] = max(lcs_dp[i-1,j], lcs_dp[i,j-1]);

# 	#below for printing

# 	i=len(s1)
# 	j=len(s2)
	
# 	res=[0]*lcs_dp[len(s1),len(s2)]
# 	l=lcs_dp[len(s1),len(s2)]-1
# 	while i>0 and j>0:
# 		if s1[i-1] == s2[j-1]:
# 			res[l]=s1[i-1]
# 			i-=1
# 			j-=1
# 			l-=1
# 		elif lcs_dp[i-1,j] > lcs_dp[i,j-1]:
# 			i-=1
# 		else:
# 			j-=1

# 	return lcs_dp[len(s1),len(s2)],''.join(res)

# s1="AGGTAB"
# s2="GXTXAYB"

# print lcs(s1,s2)
