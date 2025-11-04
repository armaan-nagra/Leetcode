class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        
        for ax, x in enumerate(cnt):
            for ay, y in enumerate(cnt):
                if not (ay <= 0.5 * ax + 7 or ay > ax or (ay > 100 and ax < 100)): #who can x send to
                    #check how many friend requests we can send?
                    if ax == ay:
                        res += x * (x - 1)
                        # res += x * (y - 1)
                    else:
                        res += x * y
        
        return res
        

        # for y in range(len(ages)):

        #     for x in range(len(ages)):
        #         if x == y:
        #             continue 
        #         if ages[y] <= 0.5 * ages[x] + 7:
        #             continue
        #         if ages[y] > ages[x]:
        #             continue 
        #         if ages[y] > 100 and ages[x] < 100:
        #             continue
        #         res += 1
        
        # return res

                



