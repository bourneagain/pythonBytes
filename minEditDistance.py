class Solution:
	# @return an integer
	def minDistance(self, word1, word2):
#     	Step 1:
# Set n to be the length of word1; Set m to be the length of word2.
# If n = 0, return m and exit.
# If m = 0, return n and exit.
# Construct a matrix containing 0...n rows and 0...m columns.

# Step 2:
# Initialize the first row to 0...n.
# Initialize the first column to 0...m.

# Step 3:
# Examine each character of word1 (i from 1 to n).

# Step 4:
# Examine each character of word2 (j from 1 to m).

# Step 5:
# If word1[i] == word2[j], the cost = 0.
# If word1[i] != word2[j], the cost = 1.

# Step 6:
# Set cell A [i, j] of the matrix equal to the minimum of:
# a) The cell immediately above plus 1: A[i - 1, j] + 1.
# b) The cell immediately to the left plus 1: A[i, j - 1] + 1.
# c) The cell diagonally above and to the left plus the cost: A[i - 1, j - 1] + cost.

# Step 7:
# After the iteration steps (3, 4, 5, 6) are complete, the distance is found in cell A[n, m].
		self.n = len(word1)
		self.m = len(word2)
		self.ar = {}

		for i in range(0,self.n+1):
			self.ar[i,0] = i
		for j in range(0,self.m+1):
			self.ar[0,j] = j
		# print self.ar
		for i in range(1,self.n+1):
			for j in range(1,self.m+1):
				l=word1[i-1]
				r=word2[j-1]
				# print i,j,l,r
				if l == r:
					self.cost = 0
				else:
					self.cost=1
					# print "diff";
				# print self.cost,self.ar[i-1,j],self.ar[i-1,j-1],self.ar[i,j-1]; 
				self.ar[i,j]=min(min(self.ar[i,j-1]+1,self.ar[i-1,j]+1),self.ar[i-1,j-1]+self.cost)
				#print "VarLUE",self.ar[i,j],"COST",self.cost
		return self.ar[self.n,self.m]

a=Solution()
print "EDIT DISTANCE = ",a.minDistance('sham','sam')