import re
def checkIP(IP):
	regex='^([2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([2][0-5][0-5]|[1]{0,1}[0-9]{1,2}$)'
	return re.match(regex,IP)

def checkIP2(n):
	return n<=255

a=['123.4.2.222', '0.0.0.0', '14.123.444.2', '1.1.1.1']
print "***** CHECK USING REGEX *****"
for IP in a:
	print IP,
	if checkIP(IP):
		print "VALID"
	else:
		print "INVALID"

print ""

print "***** CHECK USING OCTECT VALIDITY *****"
for IP in a:
	print IP,"VALID" if all([checkIP2(int(n)) for n in IP.split('.')]) else "INVALID"


checking valid email
#([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})
