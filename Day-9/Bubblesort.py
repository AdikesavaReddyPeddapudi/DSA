def bubble_sort(arr):
    n=len(arr)
    c1=0
    p1=0
    for i in range(n):
        swapped=False
        p1 += 1
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                c1 += 1
        if not swapped:
            break
    return arr,c1,p1
arr=[8,5,4,2,6,1,3]

sorted_arr1,swaps1,passes=bubble_sort(arr)
print('Sorted Array Ascending Order : ',sorted_arr1)
print("no of swaps : ",swaps1)
print("no of passes : ",passes)



def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        swapped=False
        for j in range(0, n - i - 1):
            if arr[j] % 2 ==0 and arr[j + 1]%2==0:   
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort1(arr))