#Description implementing queue using stack


class queue:
    
    def __init__(self):
        self.s1 = [] 
        self.s2 = [] 
    
    def push(self,num):
        self.s1.append(num)
    
    def pop(self):
        self.peek()
        return self.s2.pop() 

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2 

q=queue()
q.push(3)
q.push(5)
q.push(7)
print(q.peek())