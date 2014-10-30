def ss(a):
    for i in range(0,len(a)):
        smallest=i;
        for j in range(i,len(a)):
            if a[j]<a[smallest]:
                smallest=j
        a[i],a[smallest]=a[smallest],a[i]

    print a


a=[3,4,3,5,-1]
ss(a)


