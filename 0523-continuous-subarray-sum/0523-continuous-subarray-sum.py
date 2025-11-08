class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = defaultdict(int)
        rem_map[0] = -1
        total = 0
        for i, x in enumerate(nums):
            total += x
            rem = total % k
            if rem in rem_map:
                prev_index = rem_map[rem]
                if (i - prev_index) >= 2:
                    return True 
            else:
                rem_map[rem] = i
        return False
            


