class Node:
    def __init__(self, data):
        self.data = data
        self.previousNode = None
        self.nextNode = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # insert value at the end of the list
    def append(self, data):
        newNode = Node(data)

        # if the head is null it means linked list is empty
        if self.head is None:
            self.head = self.tail = newNode
        
        # else update the tail and add new node to the list
        else:
            self.tail.nextNode = newNode # update the existing tail's nextNode property
            newNode.previousNode = self.tail # update the new tail's previous node
            self.tail = newNode
            
        #update the length of list
        self.length+=1

    # insert value at the beginning on the list
    def prepend(self, data):
        newNode = Node(data)

        # if the head is None
        if self.head is None:
            self.head = self.tail = newNode

        else:
            newNode.nextNode = self.head # update the new node's next node property as previous head node
            self.head.previousNode = newNode # update the previous head node's, previousNode property as new node
            self.head = newNode # update the newly created head node and assign it

                    
        #update the length of list
        self.length+=1

        
    # display the list
    def displayForward(self):
        currentNode = self.head
        print("None < - ", end='')
        while currentNode:
            print(currentNode.data, end='')
            if not currentNode.nextNode is None:  
                print(" < = > " ,end = '')
            currentNode = currentNode.nextNode
        print(" - > None")

    # display the list in reverse
    def displayBackward(self):
        currentNode = self.tail
        print("None < - ", end='')
        while currentNode:
            print(currentNode.data, end='')
            if currentNode.previousNode:
                print(" < = > ", end='')
            currentNode = currentNode.previousNode
        print(" - > None")

    # return the size of the linked list
    def length(self):
        return self.length
        
# create an object
objDLL = Doubly_Linked_List()

# append values
objDLL.append(10)
objDLL.append(20)
objDLL.append(30)

# prepend values
objDLL.prepend(70)
objDLL.prepend(80)
objDLL.prepend(90)


# print the list
objDLL.displayForward()

# print the list in reverse order
objDLL.displayBackward()

