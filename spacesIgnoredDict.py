_end = '_end_'
import pprint
def make_trie(*words):
	root = dict()
   	for word in words:
		current_dict = root
		print word,":",
		for letter in word:
			print letter,
			print "HERE |",current_dict.setdefault(letter, {}),"|"
			current_dict = current_dict.setdefault(letter, {})
			pprint.pprint(current_dict)
			print "||||||||||||||| ",word," ||||||||DONE |||",current_dict,"_______________________________"
		current_dict = current_dict.setdefault(_end, _end)

	return root

print pprint.pprint(make_trie('sam','sad','rama'))