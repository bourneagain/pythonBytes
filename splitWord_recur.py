import sys
import pdb


class Solution():
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, d, curr_sentance=""):
        # pdb.set_trace()
        # quick check whether all chars will match (only at the begining)
        if not curr_sentance:
            sentance_chars = set(s)
            dict_chars = set("".join(list(d)))
            if not sentance_chars.issubset(dict_chars):
                return []
        if not s and curr_sentance:
            return [curr_sentance.rstrip()]
        sentances = []
        for ditem in d:
            if s.startswith(ditem):
                sentance = self.wordBreak(s[len(ditem):], d,
                                          curr_sentance + ditem + " ")
                if sentance:
                    sentances += sentance

        return sentances


# main ()
def main():
    ph = "issamsung"
    # d = {"aaaa", "aa", "a"}
    d= {'a','sam','sung','samsung','here','come','i','sam','is','the','man','he'}
    s = Solution()
    print "{}".format('\n'.join(s.wordBreak(ph, d)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
# class Solution:
# # # @param s, a string
# # # @param dict, a set of string
# # # @return a boolean
# # 	def wordBreak(self, s, dict):
# # 	    if s is None or dict is None:
# # 	        return False
# # 	    if s in dict:
# # 	        return True
# # 	    starts=[0]
# # 	    for i in range(1,len(s)+1):
# # 	        for j in range(0,len(starts)):
# # 	            if s[starts[j]:i] in dict:
# # 	                starts.insert(0,i)
# # 	                break

# # 	    return starts[0]==len(s)
# class Solution:
# 	def __init__(self):
# 		self.dic = ['sam','sung','samsung','here','come','i','sam','is','the','man','he']
		

# 	def split_word(self,a):

# 		self.split_word.__func__.h={}
# 		res = ''
# 		l=''
# 		print "HERE----------"
# 		if not a:
# 			return
# 		# if a in self.dic:
# 		# 	return a
# 		elif len(a) == 1:
# 			return 
# 		if a in self.split_word.__func__.h:
# 			return a
# 		for i in range(0,len(a)-1):
# 			pre = a[:i]
# 			suf = a[i:]
# 			#print pre,suf
# 			if pre in self.dic:
# 				self.split_word.__func__.h[pre] = True
# 				if suf in self.dic:
# 					l = l +' '+ suf
# 				l=l+ ' '+self.split_word(suf)
# 				res = pre + ' ' + l
# 		return res



# a=Solution()
# print a.split_word('samsung')   





