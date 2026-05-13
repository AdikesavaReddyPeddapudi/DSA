def search_rotated_array(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        # skip duplicates
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1

        if arr[low]<=arr[mid]: 
            if arr[low] <= target < arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:  
            if arr[mid] < target <= arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[4,5,5,9,6,7,0,1,2]
target=0
print("index : ",search_rotated_array(arr,target))