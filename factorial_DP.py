def fact(n):
  dp={}
  dp[0] = 1
  dp[1] = 1
  for i in xrange(2,n+1):
    print i
    dp[i] = i * dp[i-1]
  print dp
import time
a=time.time()
fact(20)
b=(time.time()-a)*10e5
print b




