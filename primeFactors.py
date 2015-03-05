def primes(n):
    # res = []
    # i = 2 
    # while i*i <= n:
    #     while n%i == 0:
    #         res.append(i)
    #         n=n//i
    #     i+=1
    # return res


    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
print primes(125)
