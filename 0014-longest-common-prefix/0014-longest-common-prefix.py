class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        first = strs[0]

        for i in range(len(first)):
            valid = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return res

                if first[i] != strs[j][i]:
                    valid = False
                    break
            if valid:
                res += first[i]
            else:
                break
        
        return res
            