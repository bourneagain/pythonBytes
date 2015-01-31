def countways(n):
	dp={}
	dp[0]=1
	dp[1]=1
	dp[2]=2
	for i in range(3,n+1):
		dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
	return dp[n]

def countways_recur(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	if n <0 :
		return 0
	else:
		return countways_recur(n-1)+countways_recur(n-2)+countways_recur(n-3)

print countways(30)
print countways_recur(30)