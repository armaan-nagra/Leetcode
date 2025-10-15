class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        prev = 0
        res = []
        for x in range(len(arr)):

            for y in range(prev+1, arr[x]):
                res.append(y)
            prev = arr[x]
        prev += 1
        while len(res) < k:
            res.append(prev)
            prev += 1
        print(res)

        return res[k-1]


        
