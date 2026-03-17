print("no of digits in an Array \n")
def arraycount(arr):
    count=0
    for i in arr:
        if i in arr:
            count+=1
    return count
arr=[2,4,5,7,1,3,21,8,0,45,43,6]
print("count of digits in array :",arraycount(arr))
print("Length of Array :",len(arr))

print("--------------------------------------------------------------------")
print("count of event and odd numbers in array \n")
def arraycount_even(arr):
    even1=0
    odd1=0

    for i in arr:
        if i % 2 == 0 :
            even1 += 1

        else:
            odd1 += 1
    print("even digit count in Array :",even1)
    print("odd digit count in array :",odd1)
arraycount_even(arr)

print("-------------------------------------------------------------------------------")
print("sum of two digits to get the result \n")
def twosum(arr):
    n=7
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j]==n:
                print([arr[i],arr[j]])
twosum(arr)

       
