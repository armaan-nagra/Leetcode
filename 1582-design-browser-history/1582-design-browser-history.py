class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.counter = 0
        
    def visit(self, url: str) -> None:
        self.counter += 1
        self.history = self.history[:self.counter]
        self.history.append(url)

    def back(self, steps: int) -> str:
        if self.counter < steps:
            self.counter = 0
            return self.history[self.counter]
        self.counter -= steps
        return self.history[self.counter]

    def forward(self, steps: int) -> str:
        n = len(self.history)
        if steps + self.counter >= n:
            self.counter = n - 1
            return self.history[self.counter]
        self.counter += steps
        return self.history[self.counter]
        



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)