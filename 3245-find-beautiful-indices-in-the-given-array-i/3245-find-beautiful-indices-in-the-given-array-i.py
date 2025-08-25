# class Solution:
#     def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

#         def all_occurences(text:str, pat:str) -> List[int]:
#             res = []
#             m, n = len(text), len(pat)
#             for i in range(m-n+1):
#                 if text[i:i+n] == pat:
#                     res.append(i)
#             return res
        
#         aOccurence = all_occurences(s,a)
#         bOccurence = all_occurences(s,b)

#         res = set()
#         for i in aOccurence:
#             for j in bOccurence:
#                 if abs(i - j) <= k:
#                     res.add(i)
        
#         res = sorted(res)
#         return res

from bisect import bisect_left
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def all_occurrences(text: str, pat: str) -> List[int]:
            res, m, n = [], len(text), len(pat)
            for i in range(m - n + 1):
                if text[i:i+n] == pat:
                    res.append(i)
            return res

        A = all_occurrences(s, a)
        B = all_occurrences(s, b)
        if not A or not B:
            return []

        ans = []
        for ai in A:
            # first index in B with value >= ai - k
            idx = bisect_left(B, ai - k)
            if idx < len(B) and B[idx] <= ai + k:
                ans.append(ai)
        return ans