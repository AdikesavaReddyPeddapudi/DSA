
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix

arr = [5, 10, 15, 20, 25]
print("Prefix Sum:", prefix_sum(arr))

print("------------------------index prefix sum-----------------------\n")

def prefix_sum(arr):
    prefix    = [0]*len(arr)
    prefix[0] = arr[0]

    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix
def prefix_index(prefix,L,R):
    if L==0:
        return prefix[R]
    else:
        return prefix[R]-prefix[L-1]
    return prefix_index

L=int(input("Enter the Left Index : "))
R=int(input("Enter the Right Index : "))
arr = [5,10,15,20,25]

prefix=prefix_sum(arr)
print("Array : ",arr)
print("Prefix Sum : ",prefix_sum(arr))

print("Indexed Prefix Sum: ",prefix_index(prefix,L,R))