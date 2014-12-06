import sys

with open('/tmp/query') as f:
    LINE = f.readlines()	

count_slash=0
count_quote=0
count_semicolon=0
statementList=[]
backSlashFlag=0

for char in LINE[0]:
	statementList.append(char)
	#print char + " " + str(count_quote) 
	if backSlashFlag:
		backSlashFlag=0
		continue
        
    # condition for escape quote
    
	if char == "\\":
		if backSlashFlag == 0:
			backSlashFlag=1
			continue
		else:
			backSlashFlag=0
			continue
	if char == '"' and backSlashFlag == 0:
		if count_quote == 0:
			count_quote+=1
		else:
			count_quote=0
	if char == ";" and count_quote==0:
		print "---------------------------"
		print ''.join(statementList)
		print "---------------------------"
		statementList=[]
