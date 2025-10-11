class Leaderboard:

    def __init__(self):
        self.score_map = defaultdict(int) #playerId -> score
        

    def addScore(self, playerId: int, score: int) -> None:
        self.score_map[playerId] += score

    def top(self, K: int) -> int:
        scores = []
        for x in self.score_map.values():
            scores.append(x)
        scores.sort(reverse=True)

        res = 0
        for y in range(K):
            res += scores[y]
        return res

    def reset(self, playerId: int) -> None:
        self.score_map[playerId] = 0 
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)