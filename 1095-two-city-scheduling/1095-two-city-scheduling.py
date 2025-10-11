class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        res = 0
        for x in range(n):
            costs[x].append(costs[x][0] - costs[x][1])
        
        costs.sort(key=lambda x: x[2])
        
        for x in range(n//2):
            res += costs[x][0]

        for y in range((n//2),n):
            res += costs[y][1]
        
        return res