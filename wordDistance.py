import sys
def wordDistance(alist,word1,word2):
	"""
	word distance without using extra space
	"""
	if word1 == word2:
		return 0
	minDistance=sys.maxint
	word1index=sys.maxint
	word2index=sys.maxint
	word2Found=False
	word1Found=False
	for index,word in enumerate(alist):
		if word == word1:
			word1Found=True
			word1index=index
		elif word == word2:
			word2Found=True
			word2index=index
		if word2Found and word1Found:
			distance=abs(word1index-word2index)
			if distance < minDistance:
				minDistance=distance
	return minDistance if minDistance!=sys.maxint else "NONE"


alist=["the", "quick", "brown", "fox", "quick", "test", "kumar","foxie"]
print wordDistance(alist,"x","kumar")