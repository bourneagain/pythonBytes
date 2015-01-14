import time
class Solution:
    # @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		res={}
		for index, i in enumerate(num):
			s=target-i
			if s in res:
				print res[s]+1, index+1
			else:
				res[i]=index
		return None
	def longestUniqueSubsttr(self, s):
		l={}
		n=len(s)
		i,j=0,0
		max_len=0
		while j < n:
			if s[j] in l:
				max_len = max(max_len,j-i)
				while s[i] != s[j]:
					l[s[i]] = False
					i+=1
				i+=1
				j+=1
			else:
				l[s[j]] = True
				j+=1
				
		return max_len
