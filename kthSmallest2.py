def kthSmall(A, B, k):
    """
    o(log(m)+log(n)) solution n=sizeof a ,m=sizeof b
    """
    if not A:
        return B[k]
    elif not B:
        return A[k]

    # finding median of both arrays
    ia = len(A)//2 
    ib = len(B)//2
    ma = A[ia]
    mb = B[ib]
    # idea is not to elimiate only portion of one array at a time
    if ia + ib < k:
        if ma > mb:
            return kthSmall(A,B[ib+1:],k-(ib+1))
        else:
            return kthSmall(A[ia+1:],B,k-(ia+1))
    else:
        if ma > mb:
            return kthSmall(A[:ia],B,k)
        else:
            return kthSmall(A,B[:ib],k)
b=[1,6,7,8,11,45,334]
a=[-6,-3,-2,0]

c=sorted(a+b)
k=1

print "C",c,len(c),len(c)//2,c[len(c)//2],sorted(a+b)[:k]
print kthSmall(a,b,k-1)