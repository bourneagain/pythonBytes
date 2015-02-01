class Solution:
	# @param haystack, a string
	# @param needle, a string
	# @return an integer
	def strStr_naive(self, haystack, needle):
		if not haystack and not needle:
			return 0
		if not needle and haystack:
			return 0
		if not haystack and needle:
			return -1
		j=0
		i = 0
		while i < len(haystack):
			prei = i
			while i <len(haystack) and j < len(needle) and needle[j] == haystack[i]:
				print "match",haystack[i],needle[j]
				i+=1
				j+=1
				if j == len(needle):
					return i-len(needle)
			j=0
			i = prei+1
		return -1
			
		
A = Solution()
print A.strStr_naive("aaa","aa") ;# time limit will exceed