class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the point at which this array was 'cut'
        #after that perform binary search on both subarrays

        l, r = 0, len(nums) - 1
        
        while l < r:

            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else: #nums[mid] <= nums[r]
                r = mid
        
        point = l
        firstArr = nums[0:point]
        secArr = nums[point:len(nums)]
        print(firstArr, secArr)

        l, r = 0, len(firstArr) - 1
        while l <= r:
            mid = (l+r) // 2
            if firstArr[mid] < target:
                l = mid + 1
            elif firstArr[mid] > target:
                r = mid - 1
            else:
                return mid
        
        l, r = 0, len(secArr) - 1
        while l <= r:
            mid = (l+r) // 2
            if secArr[mid] < target:
                l = mid + 1
            elif secArr[mid] > target:
                r = mid - 1
            else:
                return mid + point
        
        return -1
        






                
