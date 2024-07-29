def partition(arr,lb,ub):
    pivot=arr[lb]
    start=lb+1
    end=ub
    print(pivot,arr[lb],arr[ub],arr[start],arr[end])
    while True:
        while arr[start]<pivot and start<end:
            print(arr[start],start)
            start=start+1
        while arr[end]>=pivot and start<=end:
            print(arr[end],end)
            end=end-1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
        else:
            break
    arr[lb],arr[end]=arr[end],arr[lb]
    return end

def quickSort(arr, start, end):
    if start >= end:
        return
    k = partition(arr, start, end)
    quickSort(arr,start,k-1)
    quickSort(arr,k+1,end)

arr=[10,11,12,13,100,14,18,15]
quickSort(arr,0,len(arr)-1)

print(arr)
