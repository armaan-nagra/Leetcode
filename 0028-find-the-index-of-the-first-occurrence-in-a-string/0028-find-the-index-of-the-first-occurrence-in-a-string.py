class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLen = len(needle)
        hLen = len(haystack)
        for x in range(0, hLen - nLen + 1):
            if haystack[x:x+nLen] == needle:
                return x
        
        return -1