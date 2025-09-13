class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.n, self.f, self.l = k, -1, -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.l = (self.l+1)%self.n
            self.q[self.l] = value
            return True
        return False
        

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.f = (self.f+1)%self.n
            if self.f == self.l:
                self.f, self.l = -1, -1
            return True
        return False
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.q[(self.f+1)%self.n]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.q[self.l]
        return -1

    def isEmpty(self) -> bool:
        return self.f==-1 and self.l==-1

    def isFull(self) -> bool:
        return (self.f==self.l and self.f!=-1 and self.l!=-1) or (self.f == -1 and self.l == self.n-1)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()