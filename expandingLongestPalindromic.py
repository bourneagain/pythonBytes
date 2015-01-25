def exapandChecklps(s,l,r):
	n = len(s)
	res=''
	length=0
	while l>=0 and r <= n-1 and s[l] == s[r]:
		res=s[l:r+1]
		l-=1
		r+=1
	return res
def lps(a):
	n = len(a)
	length = 1
	for i  in range(n):
		print i,
		l1 = exapandChecklps(a,i,i)
		print "l1",l1,
		l2 = exapandChecklps(a,i,i+1)
		print "l2",l2
		length = max(length,max(len(l1),len(l2)))
	return length

print lps('ppapq')