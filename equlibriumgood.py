a=[-1, 100, 1, 98,1]
s=sum(a)
print s
ss=0
for i in range(len(a)):
    if ss == s-ss-a[i]:
        print "HERE",a[i]
    else:
        ss+=a[i]

