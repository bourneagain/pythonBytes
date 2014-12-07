dicto={}
with open('/tmp/a') as f:
	for line in f:
		s_line = line.rstrip()
		try:
			a=dicto[s_line]
		except KeyError:
			dicto[s_line]=0
			pass
		dicto[s_line]+=1
			

print dicto
