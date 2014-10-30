fibMem= {}
a="sam"
def fib(n):
	for k in range(1,n+1):
			print "k : " + str(k)
			if k<=2:
				f=1
			else:
				f=fibMem[k-1]+fibMem[k-2]
			print "printing f : " + str(f)
			fibMem[k]=f
	return fibMem[n]
print fib(1000)
#if __name__ == '__main__':
#    import timeit
#    print(timeit.timeit("print a", setup="from __main__ import *",repeat=3))
