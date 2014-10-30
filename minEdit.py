def getMinDistance( stringX, stringY ):
    if (stringX == ""):
        return len(stringY) # base case
    elif (stringY == ""):
        return len(stringX) # base case
 
    stringX = ' ' + stringX #this makes range(1,M) cover the whole string
    stringY = ' ' + stringY
    M = len(stringX)
    N = len(stringY)
    D = [ [0 for x in range(N)] for x in range(M)] #M rows and N cols
    # instead of 2d array we can also use a dict, with the key as a tuple like D[(i,j)]
    for i in range(0,M): #initialisation
        D[i][0] = i
    for j in range(0,N): #initialisation
        D[0][j] = j
    for i in range(1,M):
        for j in range(1,N):
            deletion = D[i-1][j] + 1
            insertion = D[i][j-1] + 1
            substitution =  D[i-1][j-1] + (0 if ( stringX[i] == stringY[j] ) else 2)  #cost is 2 for substitution
            D[i][j] = min( deletion, insertion, substitution )
    return D[M-1][N-1]
 
 
def main():
    assert getMinDistance( "I", "E" ) == 2
    assert getMinDistance( "INTENTION", "EXECUTION" ) == 8
    assert getMinDistance( "Hello", "Jello" ) == 2 
    assert getMinDistance( "Good", "Goodbye" ) == 3
    assert getMinDistance( "SAME", "SAME" ) == 0
    print "\nAll asserts PASSED!!, Yaaaaaay!!\n" 
 
if __name__ == "__main__":
    main()
