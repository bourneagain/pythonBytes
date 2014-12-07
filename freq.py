def GetCommonWords(book):
	wordDict=[]
	with open(book) as f:
		for line in f:
			wordList=line.split()
			for eachWord in  wordList:
				wordDict.append(eachWord)
	print len(wordDict)
	from collections import Counter
	a=Counter(wordDict)
	print a.most_common(10)

GetCommonWords('/tmp/a');
