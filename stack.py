
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(-1) 
    
    def peek(self):
        return self.stack[-1]

    def display(self):
        for i in range(len(self.stack)):
            x = len(self.stack)-1-i
            print(self.stack[x])
            x-=1
        
stack = Stack()


stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
stack.pop()
stack.display()
stack.peek()