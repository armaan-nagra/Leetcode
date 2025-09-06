class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = defaultdict(int)
        n = len(nums)
        needed = n // 3
        print(needed)

        for x in nums:
            freq[x] += 1
        print(freq)

        for value, f in freq.items():
            if f > needed:
                res.append(value)
        return res