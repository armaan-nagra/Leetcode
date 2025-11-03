class Solution:

    def __init__(self, nums: List[int]):
        self.idx = defaultdict(list)
        for i, num in enumerate(nums):
            self.idx[num].append(i)        

    def pick(self, target: int) -> int:
        indices = self.idx[target]
        return random.choice(indices)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)