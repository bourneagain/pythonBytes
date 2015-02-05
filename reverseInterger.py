import sys
class Solution:
    # @return an integer
    def reverse(self, x):   
        if list(str(x))[0] == '-':
            return int('-'+''.join(list(str(x))[1:][::-1]))
        else:
            x=int(''.join(list(str(x))[::-1]))
            if x > sys.maxint:
                return 0
            else:
                return x

aS=Solution()
x=6085774586302733229
print aS.reverse(x)
