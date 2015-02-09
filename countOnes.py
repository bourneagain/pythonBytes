def countOnes(n):
  dig=[]
  if n < 0:
    n=~n+1
  while n >=1 :
    dig.append(str(n%2))
    n=n/2
  return ''.join(dig[::-1])

import time
def countOnes2(n):
  mask=1
  #for positive
  count = 0
  itercount=0
  while n and itercount<=31: # this condition for negative
      if mask & n:
        count+=1
      n=n>>1
      itercount+=1
  return count

def countOnes3(n):
  """ o(bits) solution fastest
  """
  count = 0
  i=0
  while n and i<32:
    #time.sleep(1)
    # print n
    n= n & (n-1)
    count+=1
    i+=1
  return count


# most efficient provided some space is available:
# precompute
#http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer
def fastestCountOnes(n):
  dp = [ 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8]

  if n <= 0xff :
    return dp[n]
  elif n <= 0xffff:
    return  dp[n >> 8 ] + dp[n & 0xff]
  elif n <= 0xffffffff:
    return  dp[n & 0xff ] + dp[ (n >> 8 ) & 0xff ] + dp[(n >> 16) & 0xff]
  else:
    return dp[n & 0xff] + dp[(n >> 8) & 0xff] + dp[(n >> 16) & 0xff] + dp[(n >> 24) & 0xff];

print fastestCountOnes(70000)









