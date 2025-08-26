class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        window = []

        for i, x in enumerate(nums):
            lower = x - valueDiff
            pos = bisect_left(window, lower)
            if pos < len(window) and abs(window[pos] - x) <= valueDiff:
                return True
            
            insort(window, x)

            if i >= indexDiff:
                old = nums[i-indexDiff]
                j = bisect_left(window, old)
                window.pop(j)
            
        return False
            

