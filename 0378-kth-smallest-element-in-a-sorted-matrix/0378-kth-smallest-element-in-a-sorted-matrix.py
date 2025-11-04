class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        self.heap = [] #only keep k elements in the heap

        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                value = -matrix[r][c]
                if len(self.heap) < k:
                    heapq.heappush(self.heap, value)
                else:
                    #break if the value we want to add is larger than what is already inside
                    root = self.heap[0]
                    if value > root:
                        heapq.heapreplace(self.heap, value)
                    else:
                        break
                
        return -self.heap[0]
