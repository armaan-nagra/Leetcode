class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for x in range(32):
            res <<=1
            res = res | (n & 1) #returns whether 0 or 1 right most
            n >>= 1
        
        return res