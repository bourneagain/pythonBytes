import random,time
def merge_sort(m):
    """
     good implementation 

    """
    if len(m) <= 1:
        return m
 
    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(left,right):
	
    leftP=rightP=0
    result=[]
    while(leftP<len(left) and rightP<len(right)):
        if(left[leftP]<right[rightP]):
            result.append(left[leftP])
            leftP+=1
        else:
            result.append(right[rightP])
            rightP+=1

	print len(left),leftP,len(right),rightP
	time.sleep(2)
	print "left",  
	print left
	print "right",
	print right
	time.sleep(2)
    if left:
        result.extend(left[leftP:])

    if right:
        result.extend(right[rightP:])

    return result

#random.shuffle(A)
#aux=[]
#print A
A=[5,3,1,8,10,4]
print merge_sort(A)
