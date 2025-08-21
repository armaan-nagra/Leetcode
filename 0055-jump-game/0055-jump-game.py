class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for x in range(len(nums) -2, -1, -1):
            if nums[x] + x >= goal:
                goal = x
        
        return goal == 0
