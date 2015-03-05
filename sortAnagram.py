
import sys,pprint
def a_sort(lst):
    return sorted(lst, key=lambda elem: (sorted(elem), elem))

def a_cluster(lst):
	asp = {}
	for elem in lst:
		print "for elm",
		print elem
		sig = str(sorted(elem))
		if sig not in asp:
			asp[sig] = []
		asp[sig].append(elem)
	# print asp
	# sys.exit(0)
	result = []
	for variants in asp.values():
		result.extend(variants)
	return result

a=['god', 'dog', 'abc', 'cab', 'man']
print a
print a_sort(a)
#print a_cluster(a)

"""

for elm god
for elm dog
for elm abc
for elm cab
for elm man
{"['a', 'm', 'n']": ['man'], "['d', 'g', 'o']": ['god', 'dog'], "['a', 'b', 'c']": ['abc', 'cab']}
"""
