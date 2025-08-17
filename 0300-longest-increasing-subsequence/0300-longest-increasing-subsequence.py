class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #use dynamic programming, store the longest length of the subsequence up until that point
        n = len(nums)
        
        dp = [1] * n

        for x in range(n):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        
        return max(dp) if nums else 0


        

