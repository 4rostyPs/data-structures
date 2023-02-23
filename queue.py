class Queue():
    def __init__(self):
        self.queue = []

    def enQueue(self, value):
        self.queue.append(value)
    
    def deQueue(self):
        if len(self.queue) == 0:
            return "underflow"
        self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    def peek(self):
        return self.queue[0]



queue = Queue()
queue.deQueue()
queue.enQueue(1)
queue.enQueue(10)
queue.enQueue(8)
queue.enQueue(5)
queue.enQueue(3)
queue.enQueue(7)
queue.enQueue(4)
queue.enQueue(2)
queue.enQueue(6)
queue.enQueue(9)
queue.peek()
queue.display()
queue.deQueue()
queue.display()
queue.peek()