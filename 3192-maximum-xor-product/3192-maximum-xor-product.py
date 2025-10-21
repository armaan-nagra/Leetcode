class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 1_000_000_007

        for i in range(n-1, -1, -1):
            bit = 1 << i

            if (min(a, b) & bit) == 0:
                a^=bit
                b^=bit
            
        return (a * b) % MOD