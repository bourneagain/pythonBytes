def parens(lr,rr,_list,_str, index):
	if lr < 0 or rr < lr:
		return
	if lr == 0 and rr == 0:
		_list.append(''.join(_str))
	if lr > 0:
		_str[index]='('
		parens(lr-1,rr,_list,_str,index+1)
	if rr > 0:
		_str[index]=')'
		parens(lr,rr-1,_list,_str,index+1)
	return _list

def paren2(n):
	_str=[0]*n*2
	_list=[]
	print parens(n,n,_list,_str,0)

print paren2(3)