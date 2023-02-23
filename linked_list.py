class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insertStart(self,value):
        node = Node(value,self.head)
        self.head = node 
    def display(self):
        itr = self.head
        ll = ""
        while itr != None:
            ll += str(itr.data) + "->"
            itr = itr.next
        print(ll)
    def getLength(self):
        counter = 0
        itr = self.head
        while itr != None:
            counter += 1
            itr = itr.next
        return counter
    def addEnd(self,value):
        itr = self.head
        while itr.next != None:
            itr = itr.next
        itr.next = Node(value,None)





lList = LinkedList()
lList.insertStart(140000000000)
lList.insertStart(1234)
lList.insertStart(12345)
lList.display()
print(lList.getLength())
lList.addEnd(9)
lList.display()