def mul():
	"""12x12 multiplication table matrix"""
	for i in range(1,13):
		for j in range(1,13):
			print("{:3d}".format(i*j)),;
		print ""
mul()


