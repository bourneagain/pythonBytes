from collections import defaultdict
def permutation(str1,str2):
	str1_dict=defaultdict(lambda: 0)
	str2_dict=defaultdict(lambda: 0)
	for i in str1:
		str1_dict[i]+=1
	for j in str2:
		str2_dict[j]+=1
	if str1_dict == str2_dict:
		return True
	else:
		return False

print permutation("sama","maas");
print permutation("sama","aams");
print permutation("sama","maasa");

def permutation2(str1,str2):
	return sorted(list(str1)) == sorted(list(str2))

print permutation2("sama","maas");
print permutation2("sama","aams");
print permutation2("sama","maasa");
