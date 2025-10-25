class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        length = len(bed)

        for i in range(1, length - 1):
            if bed[i] == 0 and bed[i-1] == 0 and bed[i+1] == 0:
                bed[i] = 1
                n-=1

                if n == 0:
                    return True
            
        return n <= 0


















        # one_set = set()

        # for i, x in enumerate(flowerbed):
        #     if x == 1:
        #         one_set.add(i)
        
        # counter = 0
        # length = len(flowerbed)
        # adds = 0
        # while counter < length:
        #     if counter not in one_set and counter - 1 not in one_set and counter + 1 not in one_set:
        #         one_set.add(counter)
        #         adds += 1
        #     counter += 1
        
        # return adds >= n


