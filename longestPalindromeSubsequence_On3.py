def return_all(s):
	# this is just to get all the possible subsequences of a given string
	# o(n3) run time
	end=len(s)

	count=0
	for start in xrange(0,end):
		#print "DONE"
		lend=end
		while start!=lend:
			if len(s[start:lend])>1:
				yield s[start:lend]
			else:
				pass
			count+=1
			lend-=1


def if_palindrome(s):
	return s == s[::-1]

def lps(s):
	for sub_sequence in return_all(s):
		print sub_sequence
		# if if_palindrome(sub_sequence):
		#  	return sub_sequence

print lps('sam')
