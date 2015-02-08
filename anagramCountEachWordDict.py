
def printAnagrams(filename):
	res = {}
	with open(filename) as f:
		for word in f:
			word = word.strip()
			sort_word = ''.join(sorted(list(word)))
			print word, sort_word

			if sort_word not in res:
				res[sort_word]=[word]
			else:
				res[sort_word].append([word])
	return {k: v for k, v in res.iteritems() if len(v) == 8}

for i, j in printAnagrams('/tmp/a').iteritems():
	print i," : ",j

