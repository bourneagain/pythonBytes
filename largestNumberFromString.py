#3, 30, 34, 5, 9
def sol(a):
    res=[a[0]]
    for i in a[1:]:
        if len(res) >= len(i):
            if int(''.join(res)[:len(i)]) < int (''.join(i)):
                res.insert(0,i)
            else:
                res.append(i)
        else:
            if int(''.join(res)) > int(i[:len(res)]):
                res.append(i)
            else:
                res.insert(0,i)
        print i,res
    return res

#print sol(['3', '30', '34', '5', '9'])

def largestNumber(num):
    num = [str(x) for x in num]
    print num
    num.sort(cmp=lambda x, y: cmp(y+x, x+y))
    return ''.join(num).lstrip('0') or '0'

num=['3', '30', '34', '5', '9']
print largestNumber(num)
#return ''.join(sorted(itertools.imap(str,num), cmp=lambda x,y:cmp(y+x, x+y))).lstrip('0') or '0'

