"""
THis is a paranthesis checker 
"""
import os
import sys
os.system("clear")
#reading the path to file
if len(sys.argv) <= 1:
	print "Please input the codefile to be checked for paranthesis"
	print "USAGE : paranthesisChecker.py <path to file>"	
	sys.exit();
filename=sys.argv[1]
try:
        readme=open(filename,"r")
except IOError:
        print "*** MISSING FILE   ******* "
        print "\n"
        print "*************************************** "
        sys.exit()

openCurlBracket="{"
closedCurlBracket="}"
openBracket="("
closedBracket=")"
openSquareBracket="["
closedSquareBracket="]"
fileLines=[]

def checkSquareOpen(letter):
	if letter == openSquareBracket:
		return 1
	else:
		return 0

def checkSquareClose(letter):
	if letter == closedSquareBracket:
		return 1
	else:
		return 0

def checkOpen(letter):
	if letter == openBracket:
		return 1
	else:
		return 0

def checkClose(letter):
	if letter == closedBracket:
		return 1
	else:
		return 0

def checkCurlClose(letter):
	if letter == closedCurlBracket:
		return 1
	else:
		return 0

def checkCurlOpen(letter):
	if letter == openCurlBracket:
		return 1
	else:
		return 0

openBracketList=[]
openCurlBracketList=[]
openSquareBracketList=[]
closeBracketList=[]
closeCurlBracketList=[]
closeSquareBracketList=[]
bracketStack=list()
errorLine=1;
errorMsg=""
for lines in readme:
	##print str(errorLine) + " : reaidng line " + lines
	#print "BRACKET STACK IS :" + " ".join(bracketStack) + ":";
	for letter in lines:
		if checkOpen(letter):
			#print "open " + letter
			bracketStack.append(letter)
		if checkCurlOpen(letter):
			#print "open " + letter
			bracketStack.append(letter)
		if checkSquareOpen(letter):
			#print "open " + letter
			bracketStack.append(letter)





		#checking for closed now
		if checkClose(letter):
			#print "closing normal bracket " + letter
			try:
				type=bracketStack.pop()
				#print "pop " + type
			except IndexError:
				errorMsg+="Missing " + type + " at Line Number #" + str(errorLine) + "\n"
			if checkOpen(type) != 1:
				errorMsg+="Missing " + type + " at Line Number #" + str(errorLine) + "\n"
		if checkCurlClose(letter):
			#print "closing " + letter
			try:
				type=bracketStack.pop()
			except IndexError:
				errorMsg+="Missing " + type + " at Line Number #" + str(errorLine) + "\n"
			if not checkCurlOpen(type):
				errorMsg+="Missing " + type + " at Line Number #" + str(errorLine) + "\n"
		if checkSquareClose(letter):
			#print "closing square " + letter
			try:
				type=bracketStack.pop()
				#print "pop " + type
			except IndexError:
				errorMsg+="Missing " + type + " at Line Number #" + str(errorLine) + "\n"
			if checkSquareOpen(type) != 1:
				errorMsg+="Missing " + type + " at Line Number #" + str(errorLine) + "\n"
	errorLine+=1;


#errorMsg="No paranthesis mismatch found"
print errorMsg
if len(bracketStack):
	print "Paranthesis mismatch " + " ".join(bracketStack)
