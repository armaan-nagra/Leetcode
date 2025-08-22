class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        n = len(s)
        res = []
        anchor = -1
        maxIndex = 0
        for x in range(n):
            lastIndex[s[x]] = x

        for y in range(n):
            maxIndex = max(maxIndex, lastIndex[s[y]])
            if maxIndex == y:
                res.append(y-anchor)
                anchor = y
        
        return res

            