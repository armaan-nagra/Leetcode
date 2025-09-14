class Node:
    def __init__(self, value, minTillNow):
        self.value = value
        self.minimum = minTillNow
class MinStack:
            
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            value = Node(val,val)
        else:
            top = self.stack[-1]
            smallest = top.minimum
            if smallest < val:
                value = Node(val,smallest)
            else:
                value = Node(val,val)
        self.stack.append(value)

    def pop(self) -> None:
        return self.stack.pop().value

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()