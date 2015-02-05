import pprint,sys
def edit_distance(a,b):

	num_row=len(a)+1
	num_col=len(b)+1
	a=' '+a
	b=' '+b
	#making rows to range from 0 to num_row
	print a,b
	tb={}
	for i in range(0,num_row):
		tb[i,0]=i
	for j in range(0,num_col):
		tb[0,j]=j

	for i in range(1,num_row):
		for j in range(1,num_col):
			tb[i,j]=0
	#table set now
	#starting from 1

	#pprint.pprint(tb)
	for row in range(1,num_row):
		for col in range(1,num_col):
			if a[col-1] == b[row-1]:
				tb[row,col]=tb[row-1,col-1]
			else:
				tb[row,col]=min(tb[row,col-1]+1,tb[row-1,col]+1,tb[row-1,col-1]+1)

	print tb[len(a)-1,len(b)-1]

edit_distance('read','bed')