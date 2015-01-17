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
  while n > 0:
      if mask & n:
        count+=1
      n=n>>1
  return count

def countOnes3(n):
  """ o(bits) solution fastest
  """
  count = 0
  i=0
  while n and i<32:
    #time.sleep(1)
    print n
    n= n & (n-1)
    count+=1
    i+=1
  return count

print countOnes3(-1)
