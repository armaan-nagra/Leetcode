class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        numOfLost = defaultdict(int)

        for winner, loser in matches:
            winners.add(winner)
            losers.add(loser)
            numOfLost[loser] += 1
        
        notLost = sorted(winners - losers)
        oneLoss = []

        #iterate through numOfLost and find where value is 1, and add keys to array
        for player, losses in numOfLost.items():
            if losses == 1:
                oneLoss.append(player)
        oneLoss.sort()
        res = []
        res.append(notLost)
        res.append(oneLoss)
        return res


        