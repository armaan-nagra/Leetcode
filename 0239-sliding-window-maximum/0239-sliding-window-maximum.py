class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # #use heap, push into heap and pop to find max one at each stage?
        # l = 0
        # heap = []
        # for x in range(k):
        #     heapq.heappush(heap, (-nums[x], x))

        # res.append(-heap[0][0])

        # for r in range(k,len(nums)):
        #     heapq.heappush(heap, (-nums[r],r))
        #     l+=1
        #     while heap and heap[0][1] < l:
        #         heapq.heappop(heap)
        #     res.append(-heap[0][0])
        # return res

        res = []
        q = collections.deque() #indices
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l+=1

            r+=1
        
        return res

