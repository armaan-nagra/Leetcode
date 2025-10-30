class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = None
        n = len(nums)

        for x in range(n):
            value = nums[x]
            l, r = x + 1, n - 1

            while l < r:
                total = value + nums[l] + nums[r]
                if abs(target - total) < diff:
                    diff = abs(target - total)
                    res = total
                
                if total < target:
                    l += 1
                else:
                    r -= 1
        
        return res
                

