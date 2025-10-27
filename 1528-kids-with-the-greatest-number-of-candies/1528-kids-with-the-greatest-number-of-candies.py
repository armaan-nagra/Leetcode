class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum_candies = max(candies)
        res = []

        for x in candies:
            if x + extraCandies >= maximum_candies:
                res.append(True)
            else:
                res.append(False)
        
        return res