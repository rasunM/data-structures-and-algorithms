class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Singly_Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        # initialize the node
        newNode = Node(data)

        # check whether head is null
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.tail.nextNode = self.head
        else:
            newNode.nextNode = self.head
            self.tail.nextNode = newNode
            self.tail = newNode

        self.size+=1

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        currentNode = self.head
        while True:
            print(currentNode.data, end='')
            currentNode = currentNode.nextNode
            if currentNode == self.head:
                break
            print(end = ' - > ')
        print()

objSCLL = Singly_Circular_Linked_List()

# append values
objSCLL.append(10)
objSCLL.append(20)
objSCLL.append(30)

# display
objSCLL.display()
