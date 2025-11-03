class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        n = len(nums)
        for x in range(1, n-1):
            if nums[x] > nums[x-1] and nums[x] > nums[x+1]:
                return x
        
        if nums[n-1] > nums[n-2]:
            return n-1
