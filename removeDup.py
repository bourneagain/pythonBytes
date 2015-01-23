def removeDup(A):
    print A
    i=1
    j=0
    n = len(A)
    l = n
    while i < n:
        print l
        if A[j] < A[i]:
            j+=1
            A[j] = A[i]
        else:
            l-=1
        i+=1
    return A,l

a=[1,5,5,7,8,9,9,11]                    
print removeDup(a)