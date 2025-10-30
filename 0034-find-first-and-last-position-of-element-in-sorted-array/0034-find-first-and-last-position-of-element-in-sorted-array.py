class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #use binary search to find where one of the indices is for this and then expand outwards?

        def first_pos():
            l, r = 0, len(nums) -1
            first = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    first = mid
                    r = mid - 1
            return first

        def last_pos():
            l, r = 0, len(nums) -1
            last = -1 
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    last = mid
                    l = mid + 1
            return last 

        return [first_pos(), last_pos()] 


        
            