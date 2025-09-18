class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freqMap = defaultdict(int)
        res = 0

        for elem in words:
            rev = elem[::-1]
            if rev in freqMap and freqMap[rev] > 0:
                res += 4
                freqMap[rev] -= 1
            else:
                freqMap[elem] += 1
        used = False
        for elem, freq in freqMap.items():
            if elem == elem[::-1]:
                if freq % 2 == 0:
                    res += freq * 2
                else:
                    res += (freq // 2) * 4
                    if not used:
                        res += 2
                        used = True




        return res
