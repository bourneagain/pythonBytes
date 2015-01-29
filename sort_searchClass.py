class SortClass:
    def quick_sort(self,alist):
        self.sortme = alist
        #using a pivot 
        if len(self.sortme) <= 1:
            return self.sortme
        pivot = self.sortme[0]
        pivotlist=[]
        llist=[]
        rlist=[]
        for i in self.sortme:
            if i < pivot:
                llist.append(i)
            elif i > pivot:
                rlist.append(i)
            elif i == pivot:
                pivotlist.append(i)
        llist = self.quick_sort(llist)
        rlist = self.quick_sort(rlist)
        return llist + pivotlist + rlist

    def merge_sort(self,alist):
        # divide and conquer
        if len(alist) <= 1:
            return alist
        lleft = alist[:len(alist)//2]
        rlist = alist[len(alist)//2:]

        l = self.merge_sort(lleft)
        r = self.merge_sort(rlist)
        return self.merge(l,r)

    def merge(self, l, r):
        if not r:
            return l
        elif not l:
            return r
        res = []
        i,j = 0,0
        while i < len(l) and j<len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i+=1
            elif l[i] > r[j]:
                res.append(r[j])
                j+=1
        if i == len(l):
            res.extend(r[j:])
        else:
            res.extend(l[i:])
        return res

    def binary_search_recursive(self, alist, target):
        return self.binary_search_helper(alist, target, 0)

    def binary_search_helper(self, alist, target, ofset):
        n = len(alist)
        if n == 0:
            return -1
        elif n == 1:
            if alist[0]  == target:
                return 0+ofset
        elif n == 2:
            if alist[0]  == target:
                return 0+ofset
            elif alist[1] == target:
                return 1+ofset
            else:
                return -1

        m = n//2
        mv = alist[m]
        #recursive
        if mv == target:
            return m+ofset
        elif mv < target:
            #move right 
            return self.binary_search_helper(alist[m+1:], target, ofset+m+1)
        else:
            return self.binary_search_helper(alist[:m], target,ofset)

    def binary_search_iterative(self, alist, target):
        n = len(alist)
        if n == 0:
            return -1
        elif n == 1:
            if alist[0]  == target:
                return 0
        elif n == 2:
            if alist[0]  == target:
                return 0
            elif alist[1] == target:
                return 1
            else:
                return -1
        s,e  = 0, len(alist)-1
        while True:
            if s > e:
                return -1
            m = s+(e-s)//2
            mv = alist[m]
            if mv == target:
                return m
            elif mv < target:
                s = m+1
            else:
                e = m-1



import random,time
alist = list(set([random.randint(-10,50) for x in range(2)]))
alist = [3,4,5,6,7,8,11]
print alist

a = SortClass()        
alist = a.quick_sort(alist)
print a.binary_search_iterative(alist,13)
        

