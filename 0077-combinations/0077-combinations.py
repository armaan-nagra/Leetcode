class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i,current):
            if len(current) == k:
                res.append(current.copy())
                return
            if i > n:
                return
            current.append(i)
            backtrack(i+1,current)
            current.pop()
            backtrack(i+1,current)

        backtrack(1,[])
        return res
