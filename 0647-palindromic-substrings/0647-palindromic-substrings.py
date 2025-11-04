class Solution(object):
    def countSubstrings(self, s):
        res = 0

        for x in range(len(s)):
            res += 1
            i = x
            j, k = i - 1, i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    res += 1
                    j -= 1
                    k += 1
                else:
                    break
        
        for x in range(len(s)-1):
            a = x
            b = x + 1
            if s[a] == s[b]:
                res += 1
                c, d = a - 1, b + 1
                while c >= 0 and d < len(s):
                    if s[c] == s[d]:
                        res += 1
                        c -= 1
                        d += 1
                    else:
                        break

        return res