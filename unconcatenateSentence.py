def check_dict(_str):
	dict_=['is','a','this','man','kumar','i']
	print _str,":"
	return _str in dict_

def split_sentence(sentence):
	dp=[False]*len(sentence)
	#dp[i]: will say that that sentence[0:i] can be split into dictionary words
	for i in range(1,len(sentence)-1):
		if dp[i] == False and check_dict(sentence[0:i]):
			dp[i]=True

		if dp[i] == True:
			#check for the suffix now if valid with this prefix
			for j in range(i+1,len(sentence)):

				if dp[j] == False and check_dict(sentence[i:j]):
					dp[j] = True

				if j == len(sentence) and dp[j] == True:
					return True

	print dp
	return False

print split_sentence('ithisisa')		

