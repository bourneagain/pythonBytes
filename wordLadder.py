class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, _dict):
    	if start == end :
    		return 1
    	q=[]
    	dis={}
    	q.append(start)
    	dis[start] = 1
    	while len(q):

    		word = q.pop()
    		# print "word poped is ",word
    		if word == end :
    			break
    		for i in range(len(word)):
    			for j in range(26):
    				newword = word
    				newwordlist = list(newword)
    				newwordlist[i] = chr(ord('a') + j)
    				newword = ''.join(newwordlist)
    				# print newword,
    				if newword in _dict and newword not in dis:
    					print ">>>>>>>>>>>>>>>>>>>> ENTERED for",newword,"|",word
    					dis[newword] = dis[word] + 1
    					q.append(newword)
    			# print "appeneded"
    	print dis
    	if end not in dis:
    		return 0
    	else:
    		return dis[end]


a=Solution()
print a.ladderLength('hit',"cog",["hot","dot","dog","lot","log","cog"])
        
