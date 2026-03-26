def quick_sort(arr):
      if len(arr) <=1:
            return arr
      pivot=arr[-1]
      left=[]
      right=[]
      for i in arr[:-1]:
            if i < pivot:
                  left.append(i)
            else:
                  right.append(i)
      return quick_sort(left) + [pivot] + quick_sort(right)
arr=list(map(int,input().split()))
print(quick_sort(arr))


def quick_select(arr,k):
      return helper(arr,0,len(arr)-1,k-1)
def helper(arr,low,high,k):
      if low<=high:
            pivot_index = partition(arr,low,high)
            if pivot_index==k:
                  return arr[pivot_index]
            elif pivot_index<k:
                  return helper(arr,pivot_index+1,high,k)
            else:
                  return helper(arr,low,pivot_index-1,k)
def partition(arr,low,high):
      pivot=arr[high]
      i=low
      for j in range(low,high):
            if arr[j]<pivot:
                  arr[i],arr[j]=arr[j],arr[i]
                  i+=1
      arr[i],arr[high]=arr[high],arr[i]
      return i
k=int(input())
print(quick_select(arr,k))
