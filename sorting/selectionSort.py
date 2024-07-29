def selectionSort(arr):
    for i in range(len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[minIndex]>arr[j]:
                minIndex=j
        swapValues(arr,i,minIndex)

def swapValues(arr,firstIndex,secondIndex):
    temp=arr[firstIndex]
    arr[firstIndex]=arr[secondIndex]
    arr[secondIndex]=temp
    
arr=[12,6,7,8,10,2,9,1]
selectionSort(arr)
print(arr)
