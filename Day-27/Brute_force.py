
def two_sum(arr,target):
    result = []
    n = len(arr)-1
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                result.append((arr[i],arr[j]))
            
    return result
arr = [2,3,4,5,6,7,11,15]
target = 9
print(two_sum(arr,target))



def two_sum(arr,target):
    hashmap = {}
    for i in range(len(arr)):
        compliment = target - arr[i]   

        if compliment in hashmap:
            return (hashmap[compliment],i)

        hashmap[arr[i]] = i
    return -1
arr = [2,3,4,5,6,7,11,15]
target = 9
print(two_sum(arr,target))