def substrings(s):
    """
    Yields substrings from string s in descending order
    """
    l = len(s)
    for end in xrange(l, 0, -1):
        for start in xrange(l-end+1):
            yield s[start:start + end]
 
def palindrome(s):
    return s == s[::-1]
 
def longest_palindrome(s):
    for e in substrings(s):
        if palindrome(e):
            return e

print longest_palindrome('dabcbap')