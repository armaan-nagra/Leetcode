class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0 
        pfix = 0
        even = 0
        odd = 0

        for x in arr:
            pfix += x

            #if pfix element is odd
            if pfix % 2 != 0: 
                res += 1 + even
                odd += 1

            #pfix is even
            else:
                res += odd
                even += 1
    
         
        return res % (10**9 + 7)
        
        
        