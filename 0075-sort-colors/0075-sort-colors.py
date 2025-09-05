class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #could do bubble sort ig but O(n^2) feels unnecesary for 3 items
        n = len(nums)
        # for i in range(n):
        #     for j in range(1, n-i):
        #         if nums[j-1] > nums[j]:
        #             nums[j], nums[j-1] = nums[j-1], nums[j]
        
        #as there are only 3 items, you could potentially keep track of the pointers?
        [2,0,2,1,1,0]


        numOfOnes = 0
        numOfZeroes = 0

        for x in nums:
            if x == 0:
                numOfZeroes += 1
            if x == 1:
                numOfOnes += 1

            
        

        for x in range(n):
            if x < numOfZeroes:
                nums[x] = 0
            elif x < numOfZeroes + numOfOnes:
                nums[x] = 1
            else:
                nums[x] = 2
            


        
        

        