def test(a):
	for i in xrange(2,1111111111):
		mul = 0
		for j in range(0,32):
			if i&(1<<j):
			#	print "i:",i," j: ",j, "1<<j :",1<<j,i&(1<<j)," : ",10**j
				mul +=10**j
		# print mul
		if mul%a == 0:
			print mul
			break

test(4)		

