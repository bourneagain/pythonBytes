def countone(num):
	count=0
	while(num>=1):
		b=num%2
		if b == 1:
			count+=1			
		num=num/2
	print count
countone(8)
