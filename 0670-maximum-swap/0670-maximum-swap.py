class Solution:
    def maximumSwap(self, num: int) -> int:
        #start from left and go right and keep swapping if there's a number > it and also max
        maxMap = defaultdict(tuple)
        numstr = list(str(num))
        maxNumber = float('-inf')
        idx = None
        for x in range(len(numstr)-1,-1,-1):
            if int(numstr[x]) > maxNumber: 
                idx = x
                maxMap[x] = (int(numstr[x]), idx)
                maxNumber = int(numstr[x])
            else:
                maxMap[x] = (maxNumber,idx)

        #start from left and go right and if at any point at that index, we have a larger number, swap best to also store the index

        for y in range(len(numstr)):
            if maxMap[y][0] > int(numstr[y]):
                
                numstr[y], numstr[maxMap[y][1]] = numstr[maxMap[y][1]], numstr[y]
                return int("".join(numstr))
        
        return int("".join(numstr))

        

