def insertion_sort(arr):
    c=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and arr[j] > key:
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1]=key
        c += 1
    return arr,c
arr=[9,4,2,7,1,5]
sorted_array,count=insertion_sort(arr)
print("Sorted array:", sorted_array)
print("Number of comparisons:", count)
