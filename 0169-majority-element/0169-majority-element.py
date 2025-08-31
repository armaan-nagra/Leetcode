class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = n / 2
        occurences = defaultdict(int)

        for x in nums:
            occurences[x] += 1
        
        for item, freq in occurences.items():
            if freq > major:
                return item