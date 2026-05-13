def first_occurance(arr,target):
    low=0
    high=len(arr)-1
    result=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            result=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return result
arr=[1,2,2,3,4,5]
target=2
print("index : ",first_occurance(arr,target))


