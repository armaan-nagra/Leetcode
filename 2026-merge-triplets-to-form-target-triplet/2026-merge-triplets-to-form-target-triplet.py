class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        newTriplets = []
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            newTriplets.append([a,b,c])
        print(newTriplets)
        first = False
        second = False
        third = False

        for a, b, c in newTriplets:
            if a == target[0]:
                first = True 
            if b == target[1]:
                second = True 
            if c == target[2]:
                third = True
        return first and second and third