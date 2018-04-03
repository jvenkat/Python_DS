class Node(object):

    def __init__(self,data):
        self.data=data
        self.height=0
        self.left=None
        self.right=None

class AVL(object):

    def __init__(self):
        self.root=None

    def remove(self,data):
        if self.root:
            self.root=self.removeNode(data,self.root)

    def removeNode(self,data,node):
        if not node:
            return None
        if data<node.data:
            node.left=self.removeNode(data,node.left)
        elif data>node.data:
            node.right=self.removeNode(data,node.right)
        else:
            if not node.left and node.right:
                del node
                return None
            if not node.left:
                tempnode=node.right
                node=None
                return tempnode
            if not node.right:
                tempnode=node.left
                node=None
                return tempnode

            tempnode=self.getPre(node.left)
            node.data=tempnode.data
            node.left=self.removeNode(tempnode.data,node.left)

        if not node:
            return node

        node.height = max(self.calcHeight(node.left),self.calcHeight(node.right)) + 1
        balance=self.calcBalance(node)


        if balance > 1 and self.calcBalance(node.left)>=0:
            print("Left Left Heavy")
            return self.rotateRight(node)

        if balance<-1 and self.calcBalance(node.right)<=0:
            print("Right Right Heavy")
            return self.rotateLeft(node)

        if balance>1 and self.calcBalance(node.left)>0:
            print("Left Right Heavy")
            node.left=self.rotateLeft(node.left)
            return self.rotateRight(node)

        if balance<1 and self.calcBalance(node.right)<0:
            print("Right Left Heavy")
            node.right=self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def getPre(self,node):
        if node.rightchild:
            return self.getPre(node.rightchild)
        return node


    def insert(self,data):
        self.root=self.insertNode(data,self.root)


    def insertNode(self,data,node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left=self.insertNode(data,node.left)
        else:
            node.right=self.insertNode(data,node.right)

        node.height = max(self.calcHeight(node.left),self.calcHeight(node.right)) + 1

        return self.settleViolation(data,node)

    def settleViolation(self,data,node):
        balance=self.calcBalance(node)


        if balance > 1 and data < node.left.data:
            print("Left Left Heavy")
            return self.rotateRight(node)

        if balance<-1 and data>node.right.data:
            print("Right Right Heavy")
            return self.rotateLeft(node)

        if balance>1 and data>node.left.data:
            print("Left Right Heavy")
            node.left=self.rotateLeft(node.left)
            return self.rotateRight(node)

        if balance<1 and data<node.right.data:
            print("Right Left Heavy")
            node.right=self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self,node):

        if node.left:
            self.traverseInorder(node.left)

        print(node.data)

        if node.right:
            self.traverseInorder(node.right)



    def calcHeight(self,node):

        if not node:
            return -1
        return node.height

    def calcBalance(self,node):

        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)

    def rotateRight(self,node):
        tempnode=node.left
        t=tempnode.right
        tempnode.right=node
        node.left=t

        node.height=max(self.calcBalance(node.left),self.calcBalance(node.right))+1
        tempnode.height=max(self.calcBalance(tempnode.left),self.calcBalance(tempnode.right))+1

        return tempnode

    def rotateLeft(self,node):
        tempnode=node.right
        t=tempnode.left
        tempnode.left=node
        node.right=t

        node.height=max(self.calcBalance(node.left),self.calcBalance(node.right))+1
        tempnode.height=max(self.calcBalance(tempnode.left),self.calcBalance(tempnode.right))+1

        return tempnode

avl=AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.traverse()
avl.remove(40)
avl.traverse()
