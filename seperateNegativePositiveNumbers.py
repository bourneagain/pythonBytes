def sep(a):
    seen = False
    i=None
    for index, ele in enumerate(a):
        if ele > 0 and seen is False:
            i = index
            seen = True
        else:
            if ele < 0 and seen :
                #swap both
                a[i],a[index] = a[index],a[i]
                i+=1
    return a
import random
x=[random.randrange(-10,10,1) for x in xrange(10)]
print "ORIGINAL" , x
print "SEPERATED", sep(x)
