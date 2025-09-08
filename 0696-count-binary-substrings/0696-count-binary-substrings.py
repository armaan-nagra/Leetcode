class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        #make an array which contains the number of consecutive 0s and 1s
        curr = 1
        arr = []
        for x in range(1,len(s)):
            if s[x] == s[x-1]:
                curr += 1
            else:
                arr.append(curr)
                curr = 1
        arr.append(curr)

        for x in range(1, len(arr)):
            res += min(arr[x], arr[x-1])
        return res


        