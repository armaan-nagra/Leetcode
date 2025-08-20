class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort each interval by start
        intervals.sort(key = lambda x: x[0])
        res = []
        ans = 0
        print(intervals)

        for start, end in intervals:
            if len(res) == 0:
                res.append([start, end])
            else:
                lStart, lEnd = res[-1]
                if start >= lStart and start < lEnd:
                    ans += 1
                    if end <= lEnd:
                        res.append([start, end])
                else:
                    res.append([start, end])
        return ans


