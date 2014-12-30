from collections import defaultdict

def sz(m):
	rows=len(m)
	columns=len(m[0])
	row_list=defaultdict(lambda : False)
	col_list=defaultdict(lambda : False)
	for i in range(0,len(m)):
		for j in range(0,len(m[0])):
			if m[i][j] == 0:
				row_list[i]=True
				col_list[j]=True

	for i in range(0,len(m)):
		for j in range(0,len(m[0])):
			if row_list[i] or col_list[j]:
				m[i][j]=0
	print m

m=[[1,0,3,12],[5,6,7,8],[9,10,0,12],[13,14,15,16]]
print m
sz(m)
