"""
A code to check whether a string is palindrome or not

Example : word "radar" is palindrome : that is it means the same if spelt from right to left or otherwise
"""

#reading user input
from Dequeue import *
import sys
dString=Dequeue()
checkString=raw_input("Please enter a string to check for palindrome")
for str in checkString:
    dString.addRear(str)

#print dString.items


# check for palindrome now by poping rear and front
while not dString.isEmpty():
    try:
        if dString.delRear() == dString.delFront():
            #print "check ok"
            continue
        else:
            print "Not a palindrome"
            sys.exit()
    except IndexError:
        pass

print "String " + checkString + " is a palindrome"