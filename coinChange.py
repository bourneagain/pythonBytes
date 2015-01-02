def coin_change(coins,sum):
	 #(1, 3, 6, 7) 
	 #9
	dp={}
	dp[0]=0
	override=False
	if sum == 0:
		return 0

	for j in range(1,sum+1):
		temp=[]
		#print j
		for vi in coins:
			if vi<=j:
				temp.append(dp[j-vi])
		dp[j]=1+min(temp)
	print dp[sum]

coin_change([1,3,6,7],5)
			




