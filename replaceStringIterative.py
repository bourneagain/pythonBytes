def sol():
	inlist = ["teh", "quick", "rown", "Fox", "jmuped"]
	replacements = ["the", "quick b", "rown ", "fox", "jumped"];
	inpu = "teh quickrownFox jmuped over the lazy dog"
	ha = {}
	for index, i in enumerate(inlist):
		inpu = str.replace(inpu,i,replacements[index])

	# for index, i in enumerate(inlist):
	# 	ha[index] = "'"+str(hash(i))+"'"
	# for index, i in enumerate(inlist):
	# 	inpu = str.replace(inpu,inlist[index],ha[index])	
	# for index, i in enumerate(inlist):
	# 	inpu = str.replace(inpu,ha[index],replacements[index])
	print inpu

sol()