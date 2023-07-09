from collections import deque

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BSTNode(data)

    #inorder left subtree is visited first, followed by the root node, and then the right subtree
    def iot(self):
        elements = []
        if self.left:
            elements += self.left.iot()
        elements.append(self.data)
        if self.right:
            elements += self.right.iot()
        return elements
    
    #preorder root node is visited first, followed by the left subtree, and then the right subtree
    def preorder(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements
    
    # depth first search 
    #postorder left the left subtree is visited first, followed by the right subtree, and then the root node
    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)
        return elements
    
    # BFS -> breathe first search 
    def bfs(self):
        elements = []
        queue = deque()
        queue.append(self)
        while queue:    
            node = queue.popleft()
            elements.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return elements
    
    # search 
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # Find maximum 
    def findMax(self):
        if self.right is None:
            return self.data 
        return self.right.findMax() 
    
    # Fin minimum 
    def findMin(self):
        if self.left is None:
            return self.data 
        return self.left.data
    
    # deleting a node 
    def delete(self, val):
            if val < self.data:
                if self.left:
                    self.left = self.left.delete(val)
            elif val > self.data:
                if self.right:
                    self.right = self.right.delete(val)
            else:
                if self.left is None and self.right is None:
                    return None
                if self.left is None:
                    return self.right
                if self.right is None:
                    return self.left
                minVal = self.right.findMin()
                self.data = minVal
                self.right = self.right.delete(minVal)
            return self
        
def buildTree(elements):    
    root = BSTNode(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root

numbers = [20, 12, 7, 14, 15, 23, 27, 88]
numbersT = buildTree(numbers)
print("Inorder Traversal:", numbersT.iot())
print("Preorder Traversal:", numbersT.preorder())
print("Postorder Traversal:", numbersT.postorder())
print("BFS Traversal:", numbersT.bfs())
numbersT.delete(12)
print(numbersT.iot())
