class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        currMaxL = 0
        currMaxR = 0
        for x in range(len(height)):
            maxLeft[x] = currMaxL
            currMaxL = max(currMaxL, height[x])

        for y in range(len(height)-1, -1, -1):
            maxRight[y] = currMaxR
            currMaxR = max(currMaxR, height[y])            
        
        res = 0

        for z in range(len(height)):
            curr = min(maxLeft[z], maxRight[z]) - height[z]
            if curr > 0:
                res += curr
        return res
        