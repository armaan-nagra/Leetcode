class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # n = len(nums)
        # copy = nums[:]
        # for x in range(n):
        #     if x + k < n:
        #         nums[x+k] = copy[x]
        #     else:
        #         rem = (x + k) % n
        #         nums[rem] = copy[x]

        #reverse the array 3 times

        def rev(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        n = len(nums)
        k %= n
        rev(0,n-1)
        rev(0,k-1)
        rev(k, n-1)