class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set()
        n = len(nums)
        for i in nums:
            numbers.add(i)
        
        for j in range(n+1):
            if j not in numbers:
                return j