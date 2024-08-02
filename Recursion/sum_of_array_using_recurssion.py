def sumOfArray(index):
    if index==-1:
        return 0
    return array[index]+sumOfArray(index-1)

def mainMethod():
    global array
    array=[10,20,30,40,51]
    total=sumOfArray(len(array)-1)
    print(total)

mainMethod()
