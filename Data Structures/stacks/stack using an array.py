class Stack:
    def __init__(self, limit=100):
        self.stack = []
        self.limit = limit

    # insert data to end of the list
    def push(self, data):
        if len(self.stack) < self.limit:
            return self.stack.append(data)
        else:
            print("stack overflow")

    # pop
    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
        else:
            return self.stack.pop()

    # return the value at the top of stack
    def peek(self):
        if len(self.stack)==0:
            print("stack is empty")
            return
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack)==0

    def display(self):
        print(self.stack)

objStack = Stack()

objStack.push(10)
objStack.push(20)
objStack.push(30)
objStack.push(40)

objStack.display()

objStack.pop()

objStack.display()
