class Solution:

    def __init__(self, w: List[int]):
        self.pfix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.pfix.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        value = bisect.bisect_left(self.pfix, target)
        return value


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()