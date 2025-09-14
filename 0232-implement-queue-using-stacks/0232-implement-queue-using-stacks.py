class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        n = len(self.first)
        for x in range(n):
            value = self.first.pop()
            self.second.append(value)
        res = self.second.pop()
        n = len(self.second)
        for y in range(n):
            value = self.second.pop()
            self.first.append(value)
        return res

    def peek(self) -> int:
        n = len(self.first)
        for x in range(n):
            value = self.first.pop()
            self.second.append(value)
        res = self.second.pop()
        self.second.append(res)
        n = len(self.second)
        for y in range(n):
            value = self.second.pop()
            self.first.append(value)
        return res

    def empty(self) -> bool:
        return len(self.first) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()