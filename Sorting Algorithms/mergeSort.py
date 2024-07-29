def mergeSort(arr):
    
    if len(arr)==1:
        return arr
    
    mid=int(len(arr)/2)
    
    firstArray=mergeSort(arr[0:mid])
    secondArray=mergeSort(arr[mid:])

    return merge(firstArray,secondArray)

def merge(firstArray,secondArray):
    mix=[]
    i=0
    j=0
   

    while i<len(firstArray) and j<len(secondArray):
        if firstArray[i]<secondArray[j]:
            mix.append(firstArray[i])
            i+=1
        else:
            mix.append(secondArray[j])
            j+=1
      
     
    while i<len(firstArray):
        mix.append(firstArray[i])
        i+=1
        
    while j<len(secondArray):
        mix.append(secondArray[j])
        j+=1

 
    return mix

arr=[50,40,300,20,10]
arrReturn=mergeSort(arr)
print(arrReturn)
    
