class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for x in range(n-1, 1, -1):
            i, j = 0, x - 1
            while i < j:
                if nums[i] + nums[j] > nums[x]:
                    res += (j-i)
                    j -= 1
                else:
                    i += 1
        return res
