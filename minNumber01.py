def test(a):
	for i in xrange(2,1111111111):
		mul = 0
		for j in range(0,32):
			b=i&(1<<j)
			print i,b
			if (1<<j) > i:
				break
			if b :
			#	print "i:",i," j: ",j, "1<<j :",1<<j,i&(1<<j)," : ",10**j
				mul +=10**j

		# print mul
		# for any number ...... digit
		if (mul*9)%a == 0:
			print mul*9
			break

test(3033)		

