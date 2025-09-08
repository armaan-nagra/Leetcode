class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #prefix sums?
        n = len(nums)
        pfix = [0]
        res = 0
        for x in range(n):
            pfix.append(pfix[-1] + nums[x])
        
        pfix = pfix[1:]
        last = pfix[-1]
        for y in range(n-1):
            if pfix[y] >= (last - pfix[y]):
                res+=1
        
        return res


