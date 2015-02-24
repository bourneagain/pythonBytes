def minD(a,b,c):
	if b == c:
		return 0
	st = 99999
	seen={}
	seen[b]=False
	seen[c]=False
	min_d = 99999
	for index, i in enumerate(a):
		if i == b:
			if not seen[b]:
				seen[b] = True
			bi = index
			if seen[c]:
				min_d=min(abs(bi-ci),min_d)
		elif i == c:
			if not seen[c]:
				seen[c] = True
			ci = index
			if seen[b]:
				min_d=min(abs(bi-ci),min_d)
	if seen[b] == False or seen[c] == False:
		return -1
	return min_d				

a = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
print minD(a,3,6)