class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #need to make sure the gradient is the same for all 
        #check gradient for any two adjacent ones?

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if dy * (xi - x0) != dx * (yi - y0):
                return False 
        
        return True