from collections import deque
def firstNonRepeating(st):
	# two traversal
	c={}
	for i in range(len(st)):
		if st[i] not in c:
			c[st[i]]=0
		c[st[i]]+=1
	print c
	for i in st:
		if c[i] == 1:
			print i
			return
	return False

def firstNonRepeatingStream(st):
	q=deque()
	c={}
	for i in st:
		if i not in c:
			c[i]=0
		c[i]+=1
		q.append(i)
	while q and c[q[0]]>1:
		q.popleft()
	if not q:
		return False
	else:
		return q[0]

print firstNonRepeatingStream('geeksforgeeks')
