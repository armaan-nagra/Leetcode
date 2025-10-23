class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 0, x // 2

        while l <= r:
            mid = (l+r) // 2
            squared = mid * mid

            if squared < x:
                l = mid + 1
            elif squared > x:
                r = mid - 1
            else:
                return mid
        
        return r


