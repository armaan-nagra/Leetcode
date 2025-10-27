class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1


        while (l <= r):
            mid = l + (r - l) // 2

            value = (arr[mid] - 1 - mid)

            if value >= k:
                r = mid - 1
            elif value < k:
                l = mid + 1
            
        return arr[r] + (k-(arr[r]-1-r))
