def dpMakeChange(coinValueList,change):
	minCoins={}
	for cents in range(change+1):
		coinCount = cents
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-j] + 1 < coinCount:
				coinCount = minCoins[cents-j]+1
				coins_list=j
		minCoins[cents] = coinCount
	return minCoins[change],j


print dpMakeChange([1,5,10,21,25],15)