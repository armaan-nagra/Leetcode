class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #prefix sums?
        n = len(nums)
        pfix = 0
        res = 0
        last = sum(nums)
        for y in range(n-1):
            pfix+=nums[y]
            if pfix >= (last - pfix):
                res+=1
        
        return res


