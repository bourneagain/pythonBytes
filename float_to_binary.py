def float_to_binary(n):
	count = 0
	res = []
	res.append('.')
	f_part = n%1
	d_part = n//1
	while f_part != 0 and count < 32:
		x = f_part * 2
		f_part = x %1
		d_part = int(x)//1
		print d_part
		res.append(str(d_part))
		count += 1
	return ''.join(res)

print float_to_binary(.1)

