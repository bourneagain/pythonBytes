def check_dict(_str):
	dict_=["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"]
	return _str in dict_

def split_sentence(sentence):
	dp=[False]*(len(sentence)+1)
	#dp[i]: will say that that sentence[0:i] can be split into dictionary words
	for i in range(1,len(sentence)):
		if dp[i] == False and check_dict(sentence[0:i+1]):
			dp[i+1]=True

		if dp[i] == True:
			#check for the suffix now if valid with this prefix
			for j in range(i+1,len(sentence)+1):
				if dp[j] == False and check_dict(sentence[i:j]):
					dp[j] = True
				if j == len(sentence) and dp[j] == True:
					pass

	ll = []
	for i in range(0,len(sentence)+1):
		if dp[i] == True:
			ll.append(i)
	prev=0
	print dp
	
	for i in ll:
		print sentence[prev:i],
		prev=i

	return False

split_sentence('samsungandmango')		


