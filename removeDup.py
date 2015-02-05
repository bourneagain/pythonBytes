def removeDuplicate(a):
    for i in range(len(a)-1):
        j=i+1
        while  j < len(a)-1 and a[i] == a[j]:
            j+=1
        a[i+1]=a[j]
    return a
#print removeDuplicate([1,4,6,2,2,2,2,2,2,1])

def remove_spaces(a):
    a = bytearray(a)
    for i in range(len(a)-1):
        j=i
        if chr(a[i]) == ' ':
            i+=1
    return a
#print removeDuplicate([1,4,6,,2,2,2,2,2,1])
print remove_spaces("shyam is   is bad              a")













# def removeDup(A):
#     print A
#     i=1
#     j=0
#     n = len(A)
#     l = n
#     while i < n:
#         print l
#         if A[j] < A[i]:
#             j+=1
#             A[j] = A[i]
#         else:
#             l-=1
#         i+=1
#     return A,l

# a=[1,5,5,7,8,9,9,11]                    
# print removeDup(a)