class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        profit = 0 
        while r < n:
            if prices[l] <= prices[r]:
                profit += prices[r] - prices[l]
                l = r
                r = l + 1
            else: #prices[l] > prices[r]
                l+=1
                r+=1
        return profit
