class FreqStack:

    def __init__(self):
        self.counter = 0 
        self.items = defaultdict(list)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        self.items[f].append(val)
        if f > self.max_freq:
            self.max_freq = f
        self.counter += 1

    def pop(self) -> int:
        val = self.items[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.items[self.max_freq]:
            self.max_freq -= 1
        return val





# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()