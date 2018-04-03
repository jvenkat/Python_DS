class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class Linkedlist(object):

    def __init__(self):
        self.head=None
        self.size=0
    def insertAtBeginning(self,data):
        self.size=self.size+1
        newNode=Node(data)

        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def size(self):
        return self.size

    def insertAtEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        actualNode=self.head

        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode

        actualNode.nextNode=newNode

    def traverseList(self):
        actualNode=self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode=actualNode.nextNode

    def removeData(self,data):
        self.size=self.size-1
        actualNode=self.head
        previousNode=None

        while actualNode.data!=data:
            previousNode=actualNode
            actualNode=actualNode.nextNode

        if previousNode is None:
            self.head=actualNode.nextNode
        else:
            previousNode.nextNode=actualNode.nextNode


linkedlist = Linkedlist()
linkedlist.insertAtBeginning(12)
linkedlist.insertAtBeginning(22)
linkedlist.insertAtEnd(33)
linkedlist.traverseList()
