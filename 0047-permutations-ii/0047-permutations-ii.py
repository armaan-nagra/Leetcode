class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current, available):
            if len(available) == 0:
                res.append(current.copy())
                return

            seen = set()
            for x in range(len(available)):
                if available[x] in seen:
                    continue
                seen.add(available[x])
                value = available[x]
                backtrack(current + [value], available[:x] + available[x+1:])

        empty_list = []
        backtrack(empty_list,nums)
    
        return res


        