"""
Program to convert decimal input to binary using Stack data structure implementation
"""
from Stack import *
binaryNum=Stack()
binaryNum.size()
userInput=raw_input("Please input decimal number")
try:
	decNum = int(userInput)
except ValueError:
    print("That's not an integer!")

counter=decNum
print counter

while(counter>=1):
    #print counter%2
    binaryNum.push(counter%2)
    counter/=2
    #print "new counter"+ str(counter)

binaryString=[]
while not binaryNum.isEmpty():
    binaryString.append(binaryNum.pop())

print "Binary representation of " + str(decNum) + " is " + "".join(str(v) for v in binaryString)

