def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop() #remove the last element in the array and return it
    start_array=[]
    end_array=[]
    for item in arr:
        if item>pivot:
            end_array.append(item)
        elif item<pivot:
            start_array.append(item)
    return quickSort(start_array)+[pivot]+quickSort(end_array)
arr=[12,6,8,1,2,789,10,-1,3,600]
print(quickSort(arr))

