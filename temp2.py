import heapq
def heapSearch( bigArray, k ):
	heap = []
	# Note: below is for illustration. It can be replaced by 
	# heapq.nlargest( bigArray, k )
	word_dict = {}

	for item in bigArray:
		if item not in word_dict:
			word_dict[item] = 1
			prev = 1
		else:
			prev = word_dict[item]
			word_dict[item] += 1

		if len(heap) < k or word_dict[item] > heap[0][0]:
			
			# If the heap is full, remove the smallest element on the heap.
			if len(heap) == k: heapq.heappop( heap )
			if (prev,item) not in heap:
				heapq.heappush( heap, (prev,item) )
			else:
				i = heap.index((prev,item))
				heap[i] = (word_dict[item],item)
				heapq.heapify(heap)
			print heap,heap[0][0]
	print word_dict
	return heap

print heapSearch(['sam','kam','sam','sowbi','sam','sowbi','sowbi','sowbi','kam','kam','kam'], 2)



# #http://mathforum.org/library/drmath/view/66964.html
# def  die_game_fair_value( rolls):
#     n = rolls
#     print n
#     v={}
#     v[1] = 3.5
#     v[2] = 4.25
#     v[3] = 4.66
#     v[4] = 5.13
#     for i in range(5,n+1):
#         v[i] = (5/float(6))*float(v[i-1])+1
#     return int(v[n]*10000)
# alist = []
# while True:
#     try:
#         a = raw_input()
#         alist.append(a)
#     except (EOFError):
#         break
# countOfWords=0


# def primes(n):
#     primfac = []
#     d = 2
#     while d*d <= n:
#         while (n % d) == 0:
#             primfac.append(d)  # supposing you want multiple factors repeated
#             n //= d
#         d += 1
#     if n > 1:
#        primfac.append(n)
#     return primfac
# print primes(42)
# # import sys
# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # mappa = {'0': 0,
# #          '1': 1,
# #          '2': 2,
# #          '3': 3,
# #          '4': 4,
# #          '5': 5,
# #          '6': 6,
# #          '7': 7,
# #          '8': 8,
# #          '9': 9,
# #          'a': 10,
# #          'b': 11,
# #          'c': 12,
# #          'd': 13,
# #          'e': 14,
# #          'f': 15,
# #          'g': 16,
# #          'h': 17,
# #          'i': 18,
# #          'j': 19,
# #          'k': 20,
# #          'l': 21,
# #          'm': 22,
# #          'n': 23,
# #          'o': 24,
# #          'p': 25,
# #          'q': 26,
# #          'r': 27,
# #          's': 28,
# #          't': 29,
# #          'u': 30,
# #          'v': 31,
# #          'w': 32,
# #          'x': 33,
# #          'y': 34,
# #          'z': 35}
# # base = int(raw_input())
# # if base < 1 or base > 37:
# #     print "base invalid"
# #     sys.exit()
# # number = raw_input()
# # if not all( mappa[n] < base for n in number):
# #     print "number invalid"
# #     sys.exit()

# # newnum = list(number)
# # newnum.reverse()
# # resul = 0
# # i = 0          
# # for c in newnum:
# #     resul+=mappa[c]*(base**i)
# #     i+=1
# # print resul
	

