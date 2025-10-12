class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = float('-inf')
        
        n = len(energy)
        
        dp = [0] * n 
        for x in range(n-1, -1, -1):
            if x + k < n:
                dp[x] = energy[x] + dp[x+k]
            else:
                dp[x] = energy[x]
            res = max(dp[x], res)
        return res




            

