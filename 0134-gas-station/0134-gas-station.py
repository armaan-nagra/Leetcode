class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)

        total = 0
        start = 0
        for x in range(n):
            total += gas[x] - cost[x]
            if total < 0:
                total = 0
                start = x + 1
        return start