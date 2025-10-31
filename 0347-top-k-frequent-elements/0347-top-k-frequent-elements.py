class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) #elements -> frequency

        heap = [] #contains (frequency, element)

        for el, fr in freq.items():
            heapq.heappush(heap, (-fr, el))
        
        res = []

        for y in range(k):
            _, value = heapq.heappop(heap)
            res.append(value)
        return res
        
