def lcs(s1, s2):
	if len(s1)==0 or len(s2)==0: 
		return 0
	if s1[0] == s2[0]: 
		return 1 + lcs(s1[1:], s2[1:])
	return max(lcs(s1, s2[1:]), lcs(s1[1:], s2))

s1="AEDFHR"
s2="ABCDGH"

print lcs(s1,s2)
