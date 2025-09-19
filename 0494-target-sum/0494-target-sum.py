class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # total = sum(nums)
        # dp = [0] * (2*total + 1)
        # dp[total+1] = 1

        # for num in nums:
        #     next = [0] * len(dp)
        #     for i, cnt in enumerate(dp):
        #         if cnt == 0:
        #             continue
        #         if 0 <= i + num < len(dp):
        #             next[i+num] += cnt
        #         if 0 <= i - num < len(dp):
        #             next[i-num] += cnt
        #     dp = next
        
        # return dp[target]

        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0 
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])

            return dp[(i, total)]
        
        return backtrack(0, 0)




        


