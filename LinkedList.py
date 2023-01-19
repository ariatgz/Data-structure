
class Node:
    def __init__(self, value):
        self.value = value
        self.next= None
        self.prev= None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail= None
        self.size= 0

    def get(self, index):
        if index < 0 or index> self.size:
            return -1

        current = self.head

        while index !=0:
            current= current.next
            index = index - 1

        return current.value

    def addAtHead(self,val):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:

            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def addAtTail(self, newVal):

        newNode = Node(newVal)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail = newNode

        self.size+=1


    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return -1

        elif index == 0:
            self.addAtHead(value)

        elif index == self.size:
            self.addAtTail(value)
        else:

            prevNode = self.head

            while index >= 1:
                current = prevNode.next
                index -= 1

            newNode = Node(value)
            newNode.prev=prevNode
            newNode.next=prevNode.next
            prevNode.next.prev=newNode
            prevNode.next=newNode
            self.size +=1
    def deleteAtIndex(self,index):
        pass


