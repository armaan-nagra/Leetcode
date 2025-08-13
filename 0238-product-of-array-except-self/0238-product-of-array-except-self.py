class Solution(object):
    def productExceptSelf(self, nums):
        prefixList = []
        pCurrent = 1

        for x in nums:
            pCurrent = x * pCurrent
            prefixList.append(pCurrent)
        
        suffixList = nums
        suffixList.reverse()
        suffixes = []
        sList = 1

        for y in nums:
            sList = sList * y
            suffixes.append(sList)
        suffixes.reverse()

        res = []

        for x in range(len(nums)):
            if x == 0:
                res.append(suffixes[x+1])
            elif x == len(nums)-1:
                res.append(prefixList[x-1])
            else:
                res.append(prefixList[x-1] * suffixes[x+1])
        return res
            
            



