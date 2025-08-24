class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}

        for index, value in enumerate(nums):
            if value not in freq:
                freq[value] = index
            else:
                lastIndex = freq[value]
                if abs(index - lastIndex) <= k:
                    return True
                else:
                    freq[value] = index
        
        return False