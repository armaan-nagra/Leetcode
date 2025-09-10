class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        copy = nums[:]
        for x in range(n):
            if x + k < n:
                nums[x+k] = copy[x]
            else:
                rem = (x + k) % n
                nums[rem] = copy[x]

        