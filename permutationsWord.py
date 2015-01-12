def permutations(word): 
	print word
	if len(word) <= 1 : 
		return [word]   #get all permutations of length N-1 
	perms=permutations(word[1:]) 
	print "perms when called with word",word,perms
	char=word[0] 
	result=[] #iterate over all permutations of length N-1 
	for perm in perms: 
		for i in range(len(perm)+1): 
			print i,
			result.append(perm[:i] + char + perm[i:]) 
	return result

A='sam'
print permutations(A)