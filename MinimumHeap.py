#Implementing minimum heap using stacks

class minH:
    def __init__(self):
        self.stack=[] 
        self.minStack=[] 
    
    def push(self,num):
        self.stack.append(num)
        if self.minStack:
            num = min(num,self.minStack[-1])
        self.minStack.append(num)
    
    def pop(self):
        self.stack.pop() 
        self.minStack.pop() 
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
    
minHeap = minH()
minHeap.push(2)
minHeap.push(-2)
minHeap.push(-10)
minHeap.push(10)
print(minHeap.getMin())