class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Singly_LinkedList:
    # when the instance is creating head and tail is null
    def __init__(self):
        self.head = None
        self.tail = None

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

    def display(self):
        current = self.head

        while current:
            print(current.data, end='->')
            current = current.nextNode

        print('None')

# create object
objLL = Singly_LinkedList()

# append
objLL.append(10)
objLL.append(11)
objLL.append(12)
objLL.append(13)

# display
objLL.display()
