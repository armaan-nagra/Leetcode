class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        print(heap)
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, x)
        
        return heap[0]
