def insert_into_sorted_array(arr, x):
    arr.append(0)
    i=len(arr)-2
    while i >= 0 and arr[i] > x:
        arr[i+1]=arr[i]
        i -= 1
    arr[i+1]=x
    return arr

n=6
arr=[1,2,4,5,9]
print(insert_into_sorted_array(arr, n))