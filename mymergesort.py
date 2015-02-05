

def mergeSort(A):
	if len(A) <= 1:
		return A
	middle=len(A)//2
	leftList=A[:middle]
	rightList=A[middle:]
	leftList=mergeSort(leftList)
	rightList=mergeSort(rightList)
	return merge(leftList,rightList)

def merge(leftList,rightList):
	leftP=0;
	rightP=0;
	returnList=[]
	while leftP < len(leftList) and rightP < len(rightList):
		if leftList[leftP] < rightList[rightP]:
			returnList.append(leftList[leftP])
			leftP+=1
		else:
			returnList.append(rightList[rightP])
			rightP+=1
			
#	if leftP > len(leftList):
#		returnList.extend(rightList[rightP:])
#	if rightP > len(rightList):
#		returnList.extend(leftList[leftP:])
	if leftList:
		returnList.extend(leftList[leftP:])

	if rightList:
		returnList.extend(rightList[rightP:])
	return returnList

A=[5,1,3,53,6]
print mergeSort(A)

