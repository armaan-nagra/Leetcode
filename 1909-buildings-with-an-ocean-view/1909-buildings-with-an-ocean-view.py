class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_length = 0
        res = []
        for x in range(len(heights)-1,-1,-1):
            height = heights[x]

            if height > max_length:
                res.append(x)
                max_length = height
        res.reverse()
        return res
