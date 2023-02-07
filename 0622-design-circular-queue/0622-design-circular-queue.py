class MyCircularQueue:

    def __init__(self, k: int):
        self.stk = [None] * k
        self.front = 0
        self.rear = 0
        self.len = k

    def enQueue(self, value: int) -> bool:
        if self.stk[self.rear] == None:
            self.stk[self.rear] = value
            self.rear = (self.rear + 1) % self.len
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.stk[self.front] != None:
            self.stk[self.front] = None
            self.front = (self.front + 1) % self.len
            
            return True
        else:
            return False

    def Front(self) -> int:
        if self.stk[self.front] != None:
            return self.stk[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if self.stk[self.rear - 1] != None:
            return self.stk[self.rear - 1]
        else:
            return -1
    
    def isEmpty(self) -> bool:
        for i in range(self.len):
            if self.stk[i] != None:
                return False
        return True
        
    def isFull(self) -> bool:
        for i in range(self.len):
            if self.stk[i] == None:
                return False
        return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()