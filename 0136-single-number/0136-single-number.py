class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #perhaps you have your array nums and then loop through it 
        #at each stage you should XOR nums with your array full of that digit?
        result = 0

        for x in nums:
            result ^= x
        
        return result
        
