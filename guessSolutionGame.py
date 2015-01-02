def guessSolutionGame(guess,sol):
	guess_dict={}
	sol_dict={}

	hit=0
	phit=0
	for index,c in enumerate(sol):
		sol_dict[c]=index
	print sol_dict
	for index,c in enumerate(guess):
		try:
			if sol_dict[c] == index:
				hit+=1
		except KeyError:
			phit+=1
	return hit,phit

print guessSolutionGame('AECD','RGBY')


