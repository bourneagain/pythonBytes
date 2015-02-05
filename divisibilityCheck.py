def check():
		for i in range(1,101):
			count=0
			if i%6 == 0:
				print "divisible by 6" 
				count+=1
			if i%4 == 0:
				print "divisible by 4"
				count+=1        
			if i%24 == 0:
				print "divisble by 24"
				count+=1        
			if count == 0:
				print i

check()
