class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            arr += row
        print(arr)

        l, r = 0, len(arr) - 1

        while l<=r:
            mid = (l+r) // 2

            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid+1
            else:
                return True
        
        return False