class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #add each number in a set? and have a min and max range
        n = len(nums)
        visited = set(nums)
        
        for x in range(1, n+2):
            if x not in visited:
                return x
        