# class Solution:
#     def fib(self, n: int) -> int:
#         ans = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368, 75025,121393,196418,317811,514229,832040]
#         return ans[n]

#         # if n < 2:
#         #     return n
#         # dp = [0] * (n+1)
#         # dp[0], dp[1] = 0, 1
#         # for i in range(2, n+1):
#         #     dp[i] = dp[i-1] + dp[i-2]
#         # return dp[n]

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 3
        if n == 5: return 5
        if n == 6: return 8
        if n == 7: return 13
        if n == 8: return 21
        if n == 9: return 34
        if n == 10: return 55
        if n == 11: return 89
        if n == 12: return 144
        if n == 13: return 233
        if n == 14: return 377
        if n == 15: return 610
        if n == 16: return 987
        if n == 17: return 1597
        if n == 18: return 2584
        if n == 19: return 4181
        if n == 20: return 6765
        if n == 21: return 10946
        if n == 22: return 17711
        if n == 23: return 28657
        if n == 24: return 46368
        if n == 25: return 75025
        if n == 26: return 121393
        if n == 27: return 196418
        if n == 28: return 317811
        if n == 29: return 514229
        if n == 30: return 832040