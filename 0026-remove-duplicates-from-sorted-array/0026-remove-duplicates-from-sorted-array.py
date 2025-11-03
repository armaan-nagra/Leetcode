class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 1, 1

        while i < n:
            while i < n and nums[i] == nums[i-1]:
                i+=1
            
            if i >= n:
                break
            
            nums[j] = nums[i]
            j += 1
            i += 1
        
        return j
            



        
        




