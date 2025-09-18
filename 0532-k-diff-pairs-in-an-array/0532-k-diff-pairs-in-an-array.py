# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         pairSet = set()
#         nums.sort()
#         for x in range(len(nums)):
#             for y in range(x+1, len(nums)):
#                 if abs(nums[x] - nums[y]) == k:
#                     if (nums[x],nums[y]) not in pairSet:
#                         pairSet.add((nums[x],nums[y]))
#         print(pairSet)
#         return len(pairSet)



class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1

        nums.sort()
        res = 0
        counter = 0 

        while counter < len(nums):
            value = nums[counter]
            while counter < len(nums)-1 and value == nums[counter+1]:
                counter += 1
            
            if k == 0:
                if freq[value] >= 2:
                    res+=1
            
            else:
                if k+value in freq:
                    res += 1
            if value in freq:
                del freq[value]
            counter += 1
        
        return res
            

