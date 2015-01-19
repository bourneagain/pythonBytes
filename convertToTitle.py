import time
def convertToTitle( num):
	print num
	if num == 0:
		return ""
	else :
		return convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))

print convertToTitle(27)
print convertToTitle(703)
