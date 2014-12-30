class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
		check={}
		for index, i in enumerate(num):
			if target - i in check:
				return check[target-i]+1,index+1
			check[num[index]]=index

