class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #build adjacency list?
        adjList = defaultdict(list) #node -> [nodes it can go to]

        for x in range(len(graph)):
            adjList[x] = graph[x]

        res = []
        print(adjList)
        
        def dfs(node, current):
            if node == len(graph) - 1:
                res.append(current.copy())
            
            for x in adjList[node]:
                current.append(x)
                dfs(x, current)
                current.pop()
        
        dfs(0, [0])
        return res
