class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #sanity check 
        n = len(hand)
        if n % groupSize != 0:
            return False
        count = defaultdict(int)

        for x in hand:
            count[x] += 1
        hand.sort()

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False 
                    count[i] -=1
        
        return True