class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])
        if left == right:
            return 0
        
        for x in range(1, len(nums)):
            curr = nums[x]
            prev = nums[x-1]

            left += prev
            right -= curr

            if left == right:
                return x
        
        return -1
            
            