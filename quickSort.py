def qs(a):
    less=[]
    more=[]
    pivotList=[]
    pivot=a[0]
    if len(a)<=1:
        return a
    for i in a:
        if i<pivot:
            less.append(i)
        elif i>pivot:
            more.append(i)
        else:
            pivotList.append(i)
    more=qs(more)
    less=qs(less)
    return less+pivotList+more

a=[5,3,4,2,7,6,9]
print qs(a)
print a

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