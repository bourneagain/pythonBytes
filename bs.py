import sys
def bs(a,x):
    l=0;
#key problem area
    h=len(a)-1
#key problem area
    if len(a)<2:
        if x==a[0]:
            return 0
        else:
            return -1
    while l<=h:
#       m=(h+l)/2
 	m = l+(h-l)/2
	print m
        if x==a[m]:
            return m
        elif x<a[m]:
            h=m-1
        elif x>a[m]:
            l=m+1
    return -1

a=[0.1,1.2,1.2,3,4,5,6,7,8,9,10]
#a=[1,]
n=1.2
#print n
print bs(a,float(n))
