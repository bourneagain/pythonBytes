def titleToNumber(s):
    return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

print titleToNumber('A')








# class Solution:
#     # @param dungeon, a list of lists of integers
#     # @return a integer
#     def calculateMinimumHP(self, dungeon):

#         m = len(dungeon)
#         n = len(dungeon[0]) if m>0 else 0
#         min_hp = 1  # we need at least 1 hp to make knight alive

#         # record matrix: save the minimum hp required to enter each room and reach princess
#         record = [[0 for i in range(n)] for i in range(m)]
#         record[m-1][n-1] = min_hp if dungeon[m-1][n-1]>0 else abs(dungeon[m-1][n-1])+1  
#         # when the bottom-right room contains a number less or equal than zero, the hp required 
#         # to save the princess successfully is the absolute value of this number plus 1, 
#         # otherwise it's min_hp which equals to 1 
# 11
#         # set up the last row of the matrix backwardly
#         need = record[m-1][n-1]
#         for i in range(m-2,-1,-1):
#             record[i][n-1] = need = max(min_hp, need-dungeon[i][n-1])

#         # set up the last column of the matrix backwardly
#         need = record[m-1][n-1]
#         for i in range(n-2,-1,-1):
#             record[m-1][i] = need = max(min_hp, need-dungeon[m-1][i])

#         # fill the matrix from dungeon[m-2][n-2] to dungeon[0][0]    
#         for i in range(m-2,-1,-1):
#             for j in range(n-2,-1,-1):
#                 need = record[i][j+1] if record[i][j+1]<record[i+1][j] else record[i+1][j]  
#                 # move down or right - according to which direction has lower value
#                 record[i][j] = max(min_hp, need-dungeon[i][j]) 

#         return record[0][0]