def lis(A):
	resp=[]
	for i in range(len(A)):
		resp.append(1)

	for i in range(1,len(A)):
		print "A[i] : ",
		print A[i],
		for j in range(0,i):
			print "A[j] : ",
			print A[j]
			print "resp[i]:resp[j]",
			print resp[i],resp[j]
			if A[i] > A[j] and resp[i] < resp[j] + 1:
				resp[i]=resp[j]+1
				print "CHANGED" ,
				print resp[i],resp[j]
			print "---- END inner for"
			print ""
		print "------------------- END TOP"
		print ""
		print ""
	print "RESP below"
	print resp

A=[1, 8, 3, 4, 12] 

print A
lis(A)

#
#int maxLength = 1, bestEnd = 0;
#DP[0] = 1;
#prev[0] = -1;
#
#for (int i = 1; i < N; i++)
#{
#   DP[i] = 1;
#   prev[i] = -1;
#
#   for (int j = i - 1; j >= 0; j--)
#      if (DP[j] + 1 > DP[i] && array[j] < array[i])
#      {
#         DP[i] = DP[j] + 1;
#         prev[i] = j;
#      }
#
#   if (DP[i] > maxLength)
#   {
#      bestEnd = i;
#      maxLength = DP[i];
#   }
#}
#
