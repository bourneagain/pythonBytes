cache={}
def wordbreak(string,dictionary):
	global cache
	combo=[]
	if len(string) == 0:
		return []
	if string in cache:
		return cache[string]
	for i in range(len(string)):
		if string[:i+1] in dictionary:
			if i == len(string) -1:
				combo.append(string[:i+1])
			print "FOUND",string[:i+1]
			sub_combinations = wordbreak(string[i+1:], dictionary)
			for sub_words in sub_combinations:
				combo.append(string[:i+1]+' ' + sub_words)
	cache[string] = combo
	return combo
dictionary = ['i','like','samsung','sam','is','sung']
string = "ilikesamsung"	
print wordbreak(string,dictionary)
