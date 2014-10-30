"""
ID:rshyam.1
LANG: PYTHON 
TASK: RIDE 
"""

import sys
def checkMod(a,b):
	a=a.lower()
	b=b.lower()
	aZ={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
	suma=1
	sumb=1
	for letter in a:
		suma*=int(aZ[letter])
	print suma
	moda=suma%47
	print moda
	for letter in b:
		sumb*=int(aZ[letter])
	print sumb
	modb=sumb%47
	print modb
	if modb==moda:
		print "GO"
	else:
		print "STAY"
i,a,b=sys.argv;
checkMod(a,b)
