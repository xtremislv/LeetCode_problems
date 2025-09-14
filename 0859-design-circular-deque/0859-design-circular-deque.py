class MyCircularDeque:

    def __init__(self, k: int):
        self.n = k
        self.dq = [0] * k
        self.f, self.l = -1, -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.f, self.l = 0, 0
        else:
            self.f = (self.f-1) % self.n
        self.dq[self.f] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.f, self.l = 0, 0
        else:
            self.l = (self.l+1) % self.n
        self.dq[self.l] = value
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.f == self.l:
            self.f, self.l = -1, -1
        else:
            self.f = (self.f+1) % self.n
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.f == self.l:
            self.f, self.l = -1, -1
        else:
            self.l = (self.l-1) % self.n
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[self.f]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[self.l]
        

    def isEmpty(self) -> bool:
        return self.f == -1 and self.l == -1
        

    def isFull(self) -> bool:
        return self.l == (self.f-1) % self.n
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()