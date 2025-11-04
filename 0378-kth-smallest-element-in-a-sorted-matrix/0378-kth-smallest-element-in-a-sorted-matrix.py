class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for r in range(min(n, k)):
            heap.append((matrix[r][0], r, 0))
        heapq.heapify(heap)

        for _ in range(k - 1):
            val, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c + 1))
            
        return heap[0][0]



















        # self.heap = [] #only keep k elements in the heap

        # rows, cols = len(matrix), len(matrix[0])

        # for r in range(rows):
        #     for c in range(cols):
        #         value = -matrix[r][c]
        #         if len(self.heap) < k:
        #             heapq.heappush(self.heap, value)
        #         else:
        #             #break if the value we want to add is larger than what is already inside
        #             root = self.heap[0]
        #             if value > root:
        #                 heapq.heapreplace(self.heap, value)
        #             else:
        #                 break
                
        # return -self.heap[0]
