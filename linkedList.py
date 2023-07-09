#Description: Implementing a linked list 
#indexing : O(n)
#insert/start: O(1)
#insert/end: O(n)
#insert middle: O(n)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insertAtBeg(self,data):
        node = Node(data,self.head)
        self.head = node 
    
    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print("empty")
            return 
        itr = self.head 
        liststr = ''
        while itr:
            liststr += str(itr.data) + '-->'
            itr = itr.next
        print(liststr)

    def insertValues(self, dataList):
        self.head = None 
        for data in dataList:
            self.insertAtEnd(data)
    
    def getSize(self):
        size = 0
        itr = self.head 
        while itr:
            size += 1
            itr = itr.next
        return size 

    def removeAt(self,index):
        if index < 0 or index >=self.getSize():
            raise Exception("Not valid index")
        
        if index==0:
            self.head = self.head.next 
            return 

        count = 0
        itr = self.head 
        while itr: 
            if count == index-1:
                itr.next = itr.next.next
                return 
            itr = itr.next 
            count += 1
    
    def getAt(self, index):
        if index < 0 or index > self.getSize():
            raise Exception("invalid index")
        
        count = 0 
        itr = self.head 
        while itr:
            if count == index:
                return itr.data
            itr = itr.next 
            count += 1
        

    def insertAt(self, index, data):
        if index < 0 or index > self.getSize():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insertAtBeg(data)
            return 
        count = 0 
        itr = self.head 
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node 
                return 
            itr = itr.next 
            count += 1
    	# Get element AT
	   
    def reverse(self):
        prevNode = None 
        itr = self.head
        while itr: 
            nextNode = itr.next
            itr.next = prevNode
            prevNode = itr 
            itr = nextNode 
        self.head = prevNode   

Linkedl = LinkedList()
Linkedl.insertValues([1,2,3,4,55,999])
Linkedl.print()
print(f"Size {Linkedl.getSize()}")
print("Removing: 1")
Linkedl.removeAt(1)
Linkedl.print()
print("Getting: 2")
print("2 is at position",Linkedl.getAt(2))
print("Reversing")
Linkedl.reverse()
Linkedl.print()