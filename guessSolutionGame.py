#from collections import defaultdict
def guessSolutionGame(guess,sol):
	hit=0
	phit=0
	p={}
	for i in range(0,len(sol)):
		if guess[i] == sol[i]:
			hit+=1
		else:
			if sol[i] not in p:
				p[sol[i]]=i
			else:
				p[sol[i]]=i
	for i in range(0,len(guess)):
		if guess[i] != sol[i]:
			if guess[i] in p:
				phit+=1
				del p[guess[i]]
	return hit,phit

print guessSolutionGame('GGRR','RGBY')

