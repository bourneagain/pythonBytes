class Point():
	def __init__(self, x,y):
		self.x = x
		self.y = y

def path(m,r,c,st):
	visited={}
	pathl = 0
	for i in range(r):
		for j in range(c):
			if haspath(m, r,c, i,j, st, pathl, visited):
				return True
	return False


def haspath(m, rowC, colC, cur_row, cur_col, st, pathl, visited):
	if pathl == len(st):
		return True
	has_path_var = False
	if cur_row >= 0 and cur_row <= rowC and cur_col>=0 and cur_col<=colC and m[cur_row][cur_col] == st[pathl] and (cur_row,cur_col) not in visited:
		pathl+=1
		visited[cur_row,cur_col] = True
		has_path_var = haspath(m,rowC, colC, cur_row,cur_col-1,st,pathl,visited) or \
						haspath(m,rowC, colC, cur_row,cur_col+1,st,pathl,visited) or \
						haspath(m,rowC, colC, cur_row-1,cur_col,st,pathl,visited) or \
						haspath(m,rowC, colC, cur_row+1,cur_col,st,pathl,visited) 

		if not has_path_var:
			pathl-=1
			visited[cur_row, cur_col] = False


	return has_path_var


m=[['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]	
r = len(m)
c = len(m[0])

print path(m,r,c, ['b','c','c','e','d'])	
