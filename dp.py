memo = {}
def fib(n):
	if n in memo: 	return memo[n]
	if n<=2:
		f=1
	else:
		a=fib(n-1)
		b=fib(n-2)
		f=a+b
	memo[n]=f
	return f

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("fib(100)", setup="from __main__ import fib"))
