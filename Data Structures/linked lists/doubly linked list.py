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

    # insert at given position
    def insertAt(self, index, value):

        # if the index is the begininng of the list
        if index == 0:
            self.prepend(value)

        elif index == self.length-1:
            self.append(value)

        # check the index is with in the range of the list
        elif 1 <= index and self.length - 1 > index:
            
            newNode = Node(value)

            currentNode = self.head
            for i in range(index-1):
                currentNode = currentNode.nextNode

            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode.previousNode = newNode
            newNode.previousNode = currentNode
            currentNode.nextNode = newNode

        else :
            print("invalid length")
            return

        self.length+=1

                
    
    # return the size of the linked list
    def getLength(self):
        return self.length

    # delete at a given index
    def deleteAt(self, index):

        # check the index is not in the given range
        if index<0 or index >= self.length:
            print("Invalid Range")
            return

        if index == 0:
            self._deleteNode(self.head)

        elif index == self.length-1:
            self._deleteNode(self.tail)

        else:
            currentNode = self.head
            for i in range(index):
                currentNode = currentNode.nextNode
            self._deleteNode(currentNode)

    # delete the passed node 
    def _deleteNode(self, node):
        if node is self.head:
            self.head = node.nextNode
            # if the head is not None update the previousNode property
            if self.head is not None:
                self.head.previous = None
                
        elif node is self.tail:
            self.tail = node.previousNode
            # if the tail is not None, update the nextNode property
            if self.tail is not None:
                self.tail.nextNode = None

        else:
            node.previousNode.nextNode = node.nextNode # update the values of nodes between the current node
            node.nextNode.previousNode = node.previousNode

        # update the length
        self.length-=1
        
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

# insert at
objDLL.insertAt(2,300)

# print the list
objDLL.displayForward()

# print the list in reverse order
objDLL.displayBackward()

# delete a value at a given index
objDLL.deleteAt(3)

# print the list
objDLL.displayForward()

# print the list in reverse order
objDLL.displayBackward()

