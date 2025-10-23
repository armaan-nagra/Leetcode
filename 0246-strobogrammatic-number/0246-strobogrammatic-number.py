class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)
        pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        l, r = 0, len(num) - 1
        while l<=r:
            if num[l] not in pairs or pairs[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        
        return True

            
        


