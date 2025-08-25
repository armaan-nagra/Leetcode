class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:    
        edgeList = defaultdict(list)
        for curr, next in edges:
            edgeList[next].append(curr)

        res = []
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]

            current = set()
            values = edgeList[n]
            
            for y in values:
                current.add(y)
                current |= dfs(y)
            memo[n] = current    
            return current        
            


        for x in range(n):
            res.append(sorted(dfs(x)))
        return res