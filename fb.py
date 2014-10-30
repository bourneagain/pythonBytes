def sol(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 4
	if n>=3:
		return sol(n-1)+2*sol(n-2)+sol(n-3)


print sol(3)
