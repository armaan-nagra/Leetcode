class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.head = 0
        self.tail = -1
        self.capacity = k
        self.items = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail += 1
        if self.tail >= self.capacity:
            self.tail = self.tail % self.capacity
        self.q[self.tail] = value
        self.items += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        value = self.q[self.head]
        self.head += 1
        if self.head >= self.capacity:
            self.head = self.head % self.capacity
        self.items -=1 
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return (self.items == 0)

    def isFull(self) -> bool:
        return (self.items == self.capacity)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()