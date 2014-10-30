# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    step=0
    while(X<=Y):
        X+=D
        step+=1
    print step
solution(10,85,30)
