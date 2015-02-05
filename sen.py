ll=[]
def sol(a,st,en):
	global ll
	print a[st:en]
	dict_w=['came','cum','america','this','ok','that','hit','penny','is']
	if en > len(a):
		return None
	if a[st:en] not in dict_w:
		return sol(a,st,en+1)
	else:
		ll.append(a[st:en])
		st=en
		return sol(a,st,en)

print sol('thisisok',0,1)
print ll


