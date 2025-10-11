class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        diff = hi - lo
        arr = []
        
        for x in range(lo, hi + 1):
            value = x
            counter = 0
            while value != 1:
                if value % 2 == 0:
                    value = value // 2
                else:
                    value = (3 * value) + 1
                counter += 1
            arr.append((counter,x))
        
        arr.sort(key=lambda x: (x[0], x[1]))
        
        return arr[k-1][1]