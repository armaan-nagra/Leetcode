class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        if freq and freq.most_common(1)[0][1] > (len(s) + 1) // 2:
            return ""
        heap = []

        for ch, c in freq.items():
            heapq.heappush(heap, (-c, ch))

        res = []
        prev_count, prev_char = 0, ""

        while heap:
            count, char = heapq.heappop(heap)
            res.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            prev_count, prev_char = count + 1, char
        
        result = "".join(res)
        for i in range(1, len(result)):
            if result[i] == result[i-1]:
                return ""
        return result