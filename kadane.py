def max_sum(a):
	max_sum_so_far = a[0]
	max_sum = a[0] 
	for i in a[1:]:
		max_sum_so_far = i + max_sum_so_far
		max_sum = max(max_sum_so_far,max_sum)


a=[-2, -3, 4, -1, -2, 1, 5, -3]

print max_sum(a)