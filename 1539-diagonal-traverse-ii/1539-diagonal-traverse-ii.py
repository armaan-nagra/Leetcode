class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)

        diagonal_map = defaultdict(list)
        res = []

        for r in range(rows):
            for c in range(len(nums[r])):
                diagonal_map[r+c].append(nums[r][c])
        max_sum = max(diagonal_map.keys())
        for r in range(max_sum+1):
            if r in diagonal_map:
                diagonal_map[r].reverse()
                res.extend(diagonal_map[r])
        
        return res
        
