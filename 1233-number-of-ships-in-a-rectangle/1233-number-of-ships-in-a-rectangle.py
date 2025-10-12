# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        #split the rectangle into 4 smaller ones? and if hasShips returns False, return 0
        #else, keep splitting until the topRight = bottomLeft and if true return 1
        # right = Point(1,1)
        # left = Point(1,1)
        # print(sea.hasShips(right,left))
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
    
        res = 0

        TRX = topRight.x 
        TRY = topRight.y
        BLX = bottomLeft.x
        BLY = bottomLeft.y

        mx, my = ((TRX + BLX) // 2), ((TRY + BLY) // 2)

        res += self.countShips(sea, Point(mx, my), Point(BLX, BLY))
        res += self.countShips(sea, Point(TRX, my), Point(mx + 1, BLY))
        res += self.countShips(sea, Point(mx, TRY), Point(BLX, my + 1))
        res += self.countShips(sea, Point(TRX, TRY), Point(mx + 1, my + 1))
        
        return res
