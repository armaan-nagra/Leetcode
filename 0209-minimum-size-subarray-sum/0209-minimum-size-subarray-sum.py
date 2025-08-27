class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pfix = [0]
        res = float('inf')

        for x in range(len(nums)):
            pfix.append(nums[x] + pfix[-1])
        
        l, r = 0, 1
        print(pfix)

        while r < len(pfix):
            if pfix[r] - pfix[l] >= target:
                res = min(res, r - l)
                l += 1
            else:
                r += 1
        
        if res == float('inf'):
            return 0
        else:
            return res