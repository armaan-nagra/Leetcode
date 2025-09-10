class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        copy = nums[:]
        for x in range(n):
            if x + k < n:
                nums[x+k] = copy[x]
            else:
                rem = (x + k) % n
                print(nums[x])
                nums[rem] = copy[x]

        