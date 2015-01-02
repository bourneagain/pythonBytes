def coin_change(coins,sum):
	dp={}
	dp[0]=0
	if sum == 0:
		return 0
	for j in range(1,sum+1):
		dp[j]=1+min(dp[j-vi] for vi in coins if vi<=j)
	print dp[sum]

coin_change([1, 5, 10, 21, 25],63)
			




