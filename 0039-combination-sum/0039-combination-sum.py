class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, current):
            if total == target:
                res.append(current.copy())
                return
            if total > target or i >= len(candidates):
                return 
            current.append(candidates[i])
            backtrack(i, total + candidates[i], current)
            current.pop()
            backtrack(i + 1, total, current)
        
        backtrack(0,0,[])
        return res
