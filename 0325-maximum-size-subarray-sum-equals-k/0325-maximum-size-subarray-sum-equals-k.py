class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pfix = [nums[0]]
        for x in range(1,len(nums)):
            pfix.append(pfix[-1] + nums[x])
        
        prefixSumIdx = {0:-1}

        for y in range(len(nums)):
            if pfix[y] not in prefixSumIdx:
                prefixSumIdx[pfix[y]] = y
        
        largest = 0

        for idx, value in enumerate(pfix):
            if (value - k) in prefixSumIdx:
                largest = max(largest, idx - prefixSumIdx[value-k])
        return largest



            