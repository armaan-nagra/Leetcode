class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        #use DP, just use previous result from res, move right that many times and then increment count
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res