class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        print(total)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        
        for x in nums:

            for y in range(target, -1, -1):
                if y - x >=0:
                    dp[y] = dp[y] or dp[y-x]
        
        
        return dp[target]





























        # total = sum(nums)
        # if total % 2 != 0:
        #     return False
        
        # target = total // 2

        # dp = [False] * (target + 1)
        # dp[0] = True

        # for x in nums:
        #     for y in range(target, x - 1, -1):
        #         dp[y] = dp[y] or dp[y-x]

        # return dp[target]

