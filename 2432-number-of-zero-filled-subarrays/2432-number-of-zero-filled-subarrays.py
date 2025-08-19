class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        #find the largest subarrays of 0s and then use n(n+1) / 2 to get the amount of 0s from that
        ans = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
                ans += run
            else:
                run = 0
        return ans