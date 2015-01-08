def dpMakeChange(coinValueList,change):
	minCoins={}
	for cents in range(change+1):
		coinCount = cents
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-j] + 1 < coinCount:
				coinCount = minCoins[cents-j]+1
		print minCoins
		minCoins[cents] = coinCount
	return minCoins[change]

print dpMakeChange([1,2,3],4)