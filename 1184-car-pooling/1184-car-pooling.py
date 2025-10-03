class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #capacity empty seats
        #sort by from or index 1 in trips?

        trips.sort(key=lambda x: x[1])
        heap = [] #(end, passengers)
        riders = 0 

        for p, start, end in trips:
            while heap and heap[0][0] <= start:
                e, q = heapq.heappop(heap)
                riders -= q
            
            riders += p
            if riders > capacity:
                return False
            
            heapq.heappush(heap, (end, p))
        
        return True

        

