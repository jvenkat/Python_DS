class Node(object):

    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

class BinarySearchTree(object):

    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)

        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data < node.data:
            if node.leftchild == None:
                node.leftchild=Node(data)
            else:
                self.insertNode(data,node.leftchild)

        else:
            if node.rightchild == None:
                node.rightchild=Node(data)

            else:
                self.insertNode(data,node.rightchild)

    def remove(self,data):

        if self.root:
            self.root=self.removeNode(data,self.root)

    def removeNode(self,data,node):
        if not node:
            return node

        if data < node.data:
            node.leftchild=self.removeNode(data,node.leftchild)

        elif data > node.data:
            node.rightchild=self.removeNode(data,node.rightchild)

        else:

            if not node.leftchild and not node.rightchild:
                node=None
                return None

            if not node.leftchild:
                tempnode=node.rightchild
                node=None
                return tempnode
            elif not node.rightchild:
                tempnode=node.leftchild
                node=None
                return tempnode

            tempnode=self.getPre(node.leftchild)
            node.data=tempnode.data
            node.leftchild=self.removeNode(tempnode.data,node.leftchild)
        return node

    def getPre(self,node):
        if node.rightchild:
            return self.getPre(node.rightchild)
        return node





    def getMinval(self):

        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):

        if node.leftchild:
            return self.getMin(node.leftchild)

        return node.data

    def getMaxval(self):

        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):

        if node.rightchild:
            return self.getMax(node.rightchild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):

        if node.leftchild:
            self.traverseInorder(node.leftchild)
        print("%d", node.data)

        if node.rightchild:
            self.traverseInorder(node.rightchild)

        #print(node.data)

bst=BinarySearchTree()
#bst.insert(100)
#bst.insert(1000)
bst.insert(10)
bst.insert(0)
bst.insert(14)
bst.insert(22)
bst.traverse()
bst.remove(0)
bst.traverse()
