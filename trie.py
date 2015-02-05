
import time
def sol(_word):
	#time.sleep(1)
	print _word
	diction = ['sam','this','hit','thishit']
	if _word in diction:
		return len(_word)
	if len(_word) == 1:
		return 0
	return max(sol(_word[0]),sol(_word[1:]))

print sol('thishitn')
