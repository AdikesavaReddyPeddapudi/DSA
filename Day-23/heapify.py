
def heapify(arr, n, i):


    if right > n and arr[right] < arr[smallest]:
        smallest = right
    if 

def build_heap(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

arr = [50,30,40,10,20]
build_heap(arr)
print("Min Heap : ",arr)

