class Solution:
    def canFit(self, arr, maxWeight, days):
        currWeight = 0
        currDay = 1
        for package in arr:
            currWeight += package
            if currWeight > maxWeight:
                currDay += 1
                currWeight = package
            if currDay > days:
                return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        while l <= r:
            mid = (l + r) // 2
            if self.canFit(weights, mid, days) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l




            