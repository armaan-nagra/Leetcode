# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) < 2:
#             return 0
#         l = 0 
#         r = 1

#         max_profit = 0
#         while r < len(prices):
#             current_change = prices[r] - prices[l] 
            
#             if current_change > max_profit:
#                 max_profit = current_change
#             if prices[r] < prices[l]:
#                 l = r

#             r += 1
#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [float('inf')] * n
        if n > 0:
            dp[0] = prices[0]
        for i in range(1, n):
            dp[i] = min(dp[i-1], prices[i])
        
        maxP = -1
        for i in range(n):
            if (prices[i] - dp[i]) > maxP:
                maxP = prices[i] - dp[i]
        return maxP

