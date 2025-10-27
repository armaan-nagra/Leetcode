class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []

        if arr[0] > 1:
            missing += list(range(1, arr[0]))
        
        for x in range(len(arr) - 1):
            if arr[x] + 1 != arr[x+1]:
                missing += list(range(arr[x] + 1, arr[x+1]))

        first_done = False
        while len(missing) < k:
            if not first_done:
                value = arr[-1]
                missing.append(value + 1)
                first_done = True 
            else:
                value = missing[-1]
                missing.append(value +1)
        print(missing)                
        return missing[k-1]