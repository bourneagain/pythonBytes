addList=[1,2,10,500,-123]

def recursiveAdd(addList2):
    if len(addList2) == 1:
        return addList2[0]
    else:
        return addList2[0] + recursiveAdd(addList2[1:])

# each time we pass on the list one less than the original list ; barring the first list item


print recursiveAdd(addList)
