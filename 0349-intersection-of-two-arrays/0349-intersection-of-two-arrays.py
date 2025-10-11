class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        firstSet = set()
        for x in nums1:
            firstSet.add(x)
        
        res = set()
        for y in nums2:
            if y in firstSet:
                res.add(y)

        return list(res)