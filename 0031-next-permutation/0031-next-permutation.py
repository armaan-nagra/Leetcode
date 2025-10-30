class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        pivot = None

        for r in range(n - 1, 0, - 1):
            if nums[r] > nums[r-1]:
                pivot = r - 1
                break

        if pivot is None:
            nums.reverse()
            return 

        #find the smallest larger item
        min_value = float('inf')
        idx = None
        for x in range(pivot + 1, n):
            if nums[x] > nums[pivot]:
                if nums[x] <= min_value:
                    min_value = nums[x]
                    idx = x
        
        #swap idx and pivot and then reverse everything after pivot
        nums[idx], nums[pivot] = nums[pivot], nums[idx]
        
        #reverse everything after pivot
        l, r = pivot + 1, n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        





