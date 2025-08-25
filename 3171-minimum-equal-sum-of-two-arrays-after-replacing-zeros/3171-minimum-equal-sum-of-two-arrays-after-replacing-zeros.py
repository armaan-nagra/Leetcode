class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        aSum = sum(nums1)
        bSum = sum(nums2)
        aZeroes = 0
        bZeroes = 0
        for x in nums1:
            if x == 0:
                aZeroes += 1

        for x in nums2:
            if x == 0:
                bZeroes += 1
        
        if aZeroes == 0 and (aSum < bSum + bZeroes):
            return -1
        if bZeroes == 0 and (bSum < aSum + aZeroes):
            return -1

        return max(aSum + aZeroes, bSum + bZeroes)

