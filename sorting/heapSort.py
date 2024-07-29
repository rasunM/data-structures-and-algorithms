def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2  # Calculate the indices of the left and right children.
        largest = i

        if l < upper and lst[l] > lst[largest]:  # If left child is larger than the current node
            largest = l
        if r < upper and lst[r] > lst[largest]:  # If right child is larger than the largest so far
            largest = r

        if largest == i:  # If the largest is the current node, we're done
            break

        swap(lst, i, largest)  # Swap the current node with the largest child
        i = largest  # Continue sifting down from the largest child

def heapSort(lst):
    # Build the max-heap
    for j in range((len(lst) - 2) // 2, -1, -1):
        siftDown(lst, j, len(lst))
    
    # Extract elements from the heap
    for end in range(len(lst) - 1, 0, -1):
        swap(lst, 0, end)
        siftDown(lst, 0, end)

lst = [5, 16, 8, 14, 20, 1, 26,4]
heapSort(lst)
print(lst)  # Output: [1, 5, 8, 14, 16, 20, 26]
