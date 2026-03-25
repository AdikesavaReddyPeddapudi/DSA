
def bubble_sort_rev(arr):
    n = len(arr)
    c = 0
    p2=0
    for i in range(n):
        swapped = False
        p2 += 1
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:   # for descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                c += 1
        if not swapped:
            break

    return arr, c,p2
arr=[8,4,6,2,9]
sorted_arr, swaps,passes1 = bubble_sort_rev(arr)

print("Sorted Array (Descending):", sorted_arr)
print("Total Swaps:", swaps)
print("no of passes : ", passes1)