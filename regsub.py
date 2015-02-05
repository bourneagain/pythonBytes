import re
astr='this is a texting 123 and a number 89898 and 999end'
#regex='(a)'
regex='([0-9]+\s)'
#b=re.sub(regex,'the',astr)

#print astr[-4::1]
print re.findall(regex,astr)