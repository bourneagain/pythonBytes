def stringCombination(s):
  #print s
  _str=[]
  if len(s) == 1:
    return [s]
  perm = stringCombination(s[1:])
  c=s[0]
#  print s,perm
  for combination in perm:
    for i in range(0,len(combination)+1):
      _str.append(combination[:i]+c+combination[i:])
  return _str

a=['abc','def','ghi',]
l=[]
for i in a:
  l.append(stringCombination(''.join(i)))

#print l
for i in zip(*l):
  for j in zip(*i):
    print j

