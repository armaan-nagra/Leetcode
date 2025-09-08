class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #connect them in order of size?
        #use min-heap, add each item into this and then pop twice, add the elements together, increment counter and then push back, keep doing it until heap is empty and you can't pop the second element
        heapq.heapify(sticks)
        res = 0

        while sticks:
            first = heapq.heappop(sticks)
            if sticks:
                second = heapq.heappop(sticks)
            else:
                return res
            
            total = first + second 
            res += total 
            heapq.heappush(sticks, total)

        
