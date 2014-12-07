# idea is to scan the elments from left to right
# partition the list into two lists
# one with emtpy [ where we shall keep things sorted ] and the other the given list
# scan and swap elments in two lists

def ss(a):
    for i in range(0,len(a)-1):
        smallest=i;
        for j in range(i,len(a)):
            if a[j]<a[smallest]:
                smallest=j
        a[i],a[smallest]=a[smallest],a[i]

    print a


a=[3,4,3,5,-1]
ss(a)


