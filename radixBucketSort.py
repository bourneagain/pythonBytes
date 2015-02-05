import time
"""
very slow implementation 
"""
def radixSort( num):
	for i in range(31):
		onebucket = []
		zerobucket = []
		needle = 1 << i
		for j in range(len(num)):
			#time.sleep(1)
			if num[j] & needle != 0:
				onebucket.append(num[j])
		#		print "one",needle,num[j]
			else:
		#		print "two",needle,num[j]
				zerobucket.append(num[j])
		#print "DE",num,onebucket,zerobucket
		a=0
		for i in zerobucket:
			num[a]=i
			a+=1
		for i in onebucket:
			num[a]=i
			a+=1
		# for b in range( RADIX ):
		# 	buck = buckets[b]
		# 	for i in buck:
		# 		aList[a] = i
  #       		a += 1
		"""
		num = []
		num += zerobucket
		num += onebucket
		"""
		#print "DONE",num

	#return num
import random
import time
a=time.time()
print "START",a
print radixSort([random.randrange(0,10000) for x in xrange(1000000)])
b=time.time()-a
print "TOTAL",b
