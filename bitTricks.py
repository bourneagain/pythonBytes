def bits(n):
	while n:
		b = n & (~n+1)
		yield b
		print "b",
		print b
		print "n",
		print n
		n ^= b
		print "n after",
		print n
		print "---------------"

for b in bits(7):
    print("iter")


"""
iter
b 1
n 7
n after 6
---------------
iter
b 2
n 6
n after 4
---------------
iter
b 4
n 4
n after 0
---------------
"""
