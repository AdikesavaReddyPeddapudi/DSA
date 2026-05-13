'''
import heapq

heap = []

#Insert
heapq.heappush(heap,10)
heapq.heappush(heap,5)
heapq.heappush(heap,30)

print(heap)

# Remove Smallest
print(heapq.heappop(heap))

print(heap)
#peek
print(heap[0])

arr = [10,3,7,9,1]

heap=[]
heapq.heappush(heap,-10)
heapq.heappush(heap,-5)
heapq.heappush(heap,-20)

print(heap)

print(-heapq.heappop(heap))

print(heap)

import heapq

def k_largest(arr,k):
    return heapq.nlargest(k,arr)

print(k_largest([10,4,7,20,15],3))

def k_smallest(arr,k):
    return heapq.nsmallest(k,arr)

print(k_smallest([10,4,7,20,15],3))

'''

import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print(heap_sort([10,4,7,20,15]))