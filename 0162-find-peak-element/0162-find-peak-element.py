class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2

            #is left neighbour greater than value at mid
            if mid > 0 and nums[mid] < nums[mid-1]:
                r = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid+1]: 
                l = mid + 1
            else:
                return mid
        
            
            




















        # if len(nums) == 1:
        #     return 0

        # if nums[0] > nums[1]:
        #     return 0
        # n = len(nums)
        # for x in range(1, n-1):
        #     if nums[x] > nums[x-1] and nums[x] > nums[x+1]:
        #         return x
        
        # if nums[n-1] > nums[n-2]:
        #     return n-1
