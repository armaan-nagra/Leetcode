class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        current = []
        ret = []
        def dfs(counter):
            if counter == len(nums):
                ret.append(current.copy())
                return
            value = nums[counter]
            current.append(value)
            dfs(counter + 1)
            current.pop()
            dfs(counter + 1)

        dfs(0)

        for values in ret:
            current = 0
            for value in values:
                current ^= value
            res += current

        return res