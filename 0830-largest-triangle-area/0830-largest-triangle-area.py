class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        #a triangle can be made by just connecting any 3 points?
        def tri_area(a,b,c) -> float:
            return abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])) * 0.5 

        n = len(points)
        res = -1
        for x in range(n-2):
            for y in range(x+1, n-1):
                for z in range(y+1, n):
                    area = tri_area(points[x], points[y], points[z])
                    res = max(area, res)
        
        return res
