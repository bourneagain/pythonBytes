import heapq
def heapSearch( bigArray, k ):
    heap = []
    # Note: below is for illustration. It can be replaced by 
    # heapq.nlargest( bigArray, k )
    for item in bigArray:
    	print item
        # If we have not yet found k items, or the current item is larger than
        # the smallest item on the heap,
        if len(heap) < k or item > heap[0]:
            # If the heap is full, remove the smallest element on the heap.
            if len(heap) == k: heapq.heappop( heap )
            # add the current element as the new smallest.
            heapq.heappush( heap, item )
    return heap

print heapSearch([1,2,3,4,0,5], 2)
