def string_combinations(word):
	print "word",word
	#sam
	_str=[]
	if len(word) <= 1:
		return [word]
	perm=string_combinations(word[1:])
	print "word,perm",word,perm
	char = word[0]
	for perm in perm:
		for index in range(len(perm)+1):
			_str.append(perm[:index] + char + perm[index:])
	return _str

print string_combinations('sam')
