class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
                
        while maxHeap:
            count, char = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break 
                
                count2, value2 = heapq.heappop(maxHeap)
                res += value2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, value2))
                heapq.heappush(maxHeap, (count, char))
            else:
                res += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))
        return res
                





























        # maxHeap = [[-a, "a"], [-b, "b"], [-c, "c"]]

        # heapq.heapify(maxHeap)
        
        # res = []
        # prev = [0,None]

        # while maxHeap:
        #     count, value = heapq.heappop(maxHeap)

        #     if len(res) >= 2 and res[-1] == res[-2] == value:
        #         if not maxHeap:
        #             break 

        #         count2, value2 = heapq.heappop(maxHeap)
        #         res.append(value2)
        #         count2 += 1
        #         if count2 < 0:
        #             heapq.heappush(maxHeap, [count2, value2])
        #         heapq.heappush(maxHeap, [count, value])
        #         continue

        #     if count < -1:
        #         if res and res[-1] == value:
        #             res.append(value)
        #             count += 1
        #         else:
        #             res.append(value)
        #             res.append(value)
        #             count +=2
        #     elif count == -1:
        #         res.append(value)
        #         count = 0
            
        #     if prev[0] < 0:
        #         heapq.heappush(maxHeap, prev)

        #     prev = [count,value]
        

        # return "".join(res)




        