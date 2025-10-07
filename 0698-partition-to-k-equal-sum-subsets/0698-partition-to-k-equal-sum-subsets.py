class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False
        if total % k != 0:
            return False

        subsets = [0] * k

        def dfs(i: int) -> bool:
            if i == len(nums):
                return True 

            value = nums[i]

            for x in range(k):
                if value + subsets[x] > target:
                    continue
                subsets[x] += value
                if dfs(i+1):
                    return True
                subsets[x] -= value
                if subsets[x] == 0:
                    break
            return False
        
        return dfs(0)
            


            