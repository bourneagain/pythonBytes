"""
if s[i]==s[j] , and if i+1=j: means only two characters next to each other and both equal
make lps(i,j)=2

if s[i]==s[j] and if i+1!=j ..more characters in beteeen, then
maks lps(i,j)=lps(i+1,j-1)+2

else:
    make lps(i,j)=max(lps(i,j-1),lps(i+1,j))
"""

def lps_dp(s):
    #taking exmaple of dabcbap : len 7 inner loop i is from 0 to 5 
    n=len(s)
    lps={}
    #making lps(i,i)=1
    for i in xrange(len(s)):
        lps[i,i]=True

    for char_count in xrange(2, n+1):
        #means count of the palindrom sub sequence can be 2 to entire length of string
        for i in xrange(0, n - char_count+1):
            j = i + char_count - 1
            print i,char_count, j ,n,"|",
            if s[i] == s[j] and char_count == 2:
                lps[i,j] = 2
            elif s[i] == s[j]:
                lps[i,j] = lps[i+1,j-1] + 2
            else:
                lps[i,j] = max(lps[i,j-1],lps[i+1,j])
        print ""
    # below for printing the sequence
    for k in lps:
        i,j=k
        if i+5 == j and s[i] == s[j-1]:
            print s[i:j]
    return lps[0,n-1]


print lps_dp('dabcbap')

