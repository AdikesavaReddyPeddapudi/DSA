'''

def two_sum(arr,target):
    left = 0
    right = len(arr)-1
    result = []
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            result.append((arr[left],arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return result
arr=[1,2,3,4,5,6,7,8,9]
target=8
print(two_sum(arr,target))      



def reverse(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr
arr = [1,2,3,4,5,6,7]
print(reverse(arr))


def remove_duplicates(arr):
    if not arr:
        return 0
    arr.sort()
    i=0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1
arr = [1,6,2,4,3,3,4,5,6,7,7,7,8]
length= remove_duplicates(arr)
print(arr[:length])

'''
def max_sum(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k,len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        max_sum = max(max_sum,window_sum)
    return max_sum
arr = [2,1,5,1,3,2,6]
k=3
print(max_sum(arr,k))

