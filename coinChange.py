def coin_change(coinlist, change):
	dp=[x for x in range(0,change+1)]
	# dp 0 indicating best solution for change 0
	# assuming one is there in coinlist

	for changes in range(1,change+1):
		# so far solution for changes that we can make is using 1
		for coin_availabe in [ x for x in coinlist if x <= changes ] :
			if dp[changes - coin_availabe]+1 < dp[changes]:
				dp[changes]=dp[changes - coin_availabe]+1
	return dp[change]

print coin_change([1, 5, 10,21,25],63)


