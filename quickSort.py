def qs(a):
    less=[]
    more=[]
    pivotList=[]
    if len(a)<=1:
        return a
    pivot=a[0]
    for i in a:
        if i<pivot:
            less.append(i)
        elif i>pivot:
            more.append(i)
        else:
            pivotList.append(i)
    less=qs(less)
    more=qs(more)
    return less+pivotList+more

a=[3,3,3,3,3,8]
print a
print qs(a)

# def quickSort(arr):
#     less = []
#     pivotList = []
#     more = []
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         for i in arr:
#             if i < pivot:
#                 less.append(i)
#             elif i > pivot:
#                 more.append(i)
#             else:
#                 pivotList.append(i)
#         less = quickSort(less)
#         more = quickSort(more)
#         return less + pivotList + more
 
# a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
# a = quickSort(a)
