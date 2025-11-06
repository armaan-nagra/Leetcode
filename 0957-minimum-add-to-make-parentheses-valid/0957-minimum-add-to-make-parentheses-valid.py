class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openB = 0
        needOpen = 0

        for x in s:
            if x == "(":
                openB += 1
            else: # x == ")"
                if openB:
                    openB -= 1
                else:
                    needOpen += 1

        return openB + needOpen 