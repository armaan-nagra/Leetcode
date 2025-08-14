class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for x in range(n):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            target = -nums[x]
            l = x + 1
            r = n - 1
            
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[x],nums[l],nums[r]])

                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

                elif s < target:
                    l+=1
                else:
                    r-=1
        return res 
                










