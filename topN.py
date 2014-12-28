from collections import defaultdict,Counter
# default dict can help pass a default value to key incase it does not exist
import time

def topN_words(filename):
	op_dict=defaultdict(lambda: 1)
	try:
		with open(filename) as f:
			pass
	except IOError:
		print "FILE ERROR"

	with open(filename) as f:
		for lines in f:
			for words in lines.split():
				word=words.strip()
				if len(word) > 3:
					op_dict[word]+=1
	print "done but waiting to check memory"
	# counter can pull most common and return
	# memory in this case is only limited by unique words on the file
	# also with the "with open" memory does not require entire file to be loaded
	res=op_dict
	a=raw_input('ok done' + str(len(res)))
	res=Counter(op_dict).most_common(3)[0][0]
	return res
print topN_words('/tmp/a') 
# shakespear work in /tmp/a
