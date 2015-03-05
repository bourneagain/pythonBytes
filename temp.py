import math,time
def is_prime(number):
  if number > 1:
    if number == 2:
      return True
    if number % 2 == 0:
      return False
    for i in xrange(3,int(math.sqrt(number))+1):
      if number % i == 0:
        return False
    return True
  else:
    return False

def get_primes(number): 
  while True: 
    if is_prime(number): 
      yield number 
    number += 1

for i in get_primes(2):
  print i
  time.sleep(1)