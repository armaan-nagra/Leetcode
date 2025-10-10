class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        bobValue = 0
        aliceValue = 0
        heap = []

        for i in range(n):
            heapq.heappush(heap, (-(aliceValues[i] + bobValues[i]), i))
        
        alice_turn = True 

        while heap:
            _, i = heapq.heappop(heap)
            if alice_turn:
                aliceValue += aliceValues[i]
            else:
                bobValue += bobValues[i]
            alice_turn = not alice_turn 
        
        if aliceValue > bobValue:
            return 1
        elif bobValue > aliceValue:
            return -1
        else:
            return 0



        
        
            



        
        
        



