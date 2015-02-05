def findSubstring( S, L):
    """ The idea is very simple, use brute-force with hashing. 
    First we compute the hash for each word given in L and add them up. 
    Then we traverse from S[0] to S[len(S) - total_length], for each index, i
    f the first substring in L, then we compute the total hash for that partition, 
    if hashes match, then we have a match.
    """
    if S is None or L is None or len(L) == 0:
        return []
    # the length of each word
    len_of_word = len(L[0])
    # the length of entire substring
    total_length = len_of_word * len(L)
    # use a set to reduce lookup time
    word_set = set(L)
    # total hash for the given list of words
    target_hash = 0
    for item in L:
        target_hash += hash(item)
    ret = []
    for start in xrange(len(S) - total_length + 1):
        if S[start:start+len_of_word] not in word_set:
            continue
        end = start + total_length - 1
        test_hash = 0
        for walker in xrange(start, end + 1, len_of_word):
            substring = S[walker:walker + len_of_word]
            # early termination if any of the substring not in set
            if substring not in word_set:
                break
            test_hash += hash(substring)
        if test_hash == target_hash:
            ret.append(start)
    return ret
print findSubstring('shsamsampamasdasdpamsam',['sam','pam'])