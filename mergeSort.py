import random
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

    if left:
        result.extend(left[leftP:])

    if right:
        result.extend(right[rightP:])

    return result


A=range(1000000)
random.shuffle(A)
#aux=[]
#print A
print merge_sort(A)
