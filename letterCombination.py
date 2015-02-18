mapp = {}
mapp['2']=['a','b','c']
mapp['3']=['d','e','f']
def letterCombination(digits):
	n = len(digits)
	cs = [0]*n
	res=[]
	appendd(digits, 0 ,cs, res )
	return res

def appendd(digits, i, cs, res):
	if i == len(digits):
		res.extend(cs)
		res.append('#')
		print "RES",res
		return
	letters=mapp[digits[i]]
	for index,j in enumerate(letters):
		cs[i] = letters[index]
		appendd(digits, i+1, cs, res)

print letterCombination(['2','3'])