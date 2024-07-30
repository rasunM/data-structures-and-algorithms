class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Singly_LinkedList:
    # when the instance is creating head and tail is null
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # add value to end of the list
    def append(self, data):

        # create a new node from the Node class
        newNode = Node(data)

        # check whether the head is null
        if self.head is None:
            self.head = newNode
            self.tail = self.head

        else:
            self.tail.nextNode = newNode # assign the newNode to the previous tail's next node
            self.tail = newNode # update the tail

        # increment the length
        self.length+=1

    # insert value at the beginning
    def prepend(self, data):

        # create a node
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            self.tail = self.head

        else:
            newNode.nextNode = self.head
            self.head = newNode

        # increment the length
        self.length+=1

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end='->')
            current = current.nextNode

        print('None')

    def insertAt(self, position, data):

        # check whether the index is in the bound of the list
        if 0 > position or self.length <= position:
            return None

        elif position == 0:
            self.prepend(data)

        elif position == self.length-1 :
            self.append(data)

        else:
            # create a node
            newNode = Node(data)

            current = self.head
            
            for i in range(position-1):
                current = current.nextNode

            newNode.nextNode = current.nextNode
            current.nextNode = newNode

            # increment the length
            self.length+=1
            
    # Delete an  item at the end
    def deleteAt(self, index):

        # check the list is empty
        if self.head is None:
            print("Linked list is empty")
            return 

        # remove the first index
        elif index == 0 :
            
            self.head = self.head.nextNode

            self.length-=1

            if self.head is None: # If list is empty the tail shold be update
                self.tail = None


        # check the index in range
        elif 0<=index and index <= self.length - 1 :
            
            previousNode = self.head
            for i in range(index-1):
                previousNode = previousNode.nextNode # get the previous Node

            # assign the node before the index node, to the node after the index node
            nodeToDelete = previousNode.nextNode
            previousNode.nextNode = nodeToDelete.nextNode

            # check whether the deleted node is the last node
            if nodeToDelete == self.tail:
                self.tail = previousNode # update the tail
            
            self.length-=1

        # index out of bounds
        else:
            print("Index out of bounds")


    # search a value
    def search(self, value):
        currentNode = self.head

        for i in range(self.length):
                
            # check whether the current node's value is equal to the searched value
            if currentNode.data == value:
                return True
                
            currentNode = currentNode.nextNode

        # value does not found  
        else:
            return False
            

# create object
objLL = Singly_LinkedList()

# append
objLL.append(10)
objLL.append(11)
objLL.append(12)
objLL.append(13)

# prepend
objLL.prepend(20)
objLL.prepend(21)

# display
objLL.display()

# delete At
objLL.deleteAt(2)

# display
objLL.display()

# delete At
objLL.deleteAt(0)

# display
objLL.display()

# get the length
length = objLL.length
print(length)

# check whether, an element is in the list
status1 = objLL.search(12)
print(status1)

status2 = objLL.search(44)
print(status2)
