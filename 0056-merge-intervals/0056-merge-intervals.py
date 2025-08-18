class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by first item in list?
        intervals.sort(key=lambda x:x[0])
        res = []

        for low, high in intervals:
            if len(res) == 0:
                res.append([low, high])
            else:
                currL, currR = res[-1]
                if low >= currL and low <= currR:
                    res.pop()
                    res.append([currL, max(currR, high)])
                else:
                    res.append([low, high])
        
        return res

        