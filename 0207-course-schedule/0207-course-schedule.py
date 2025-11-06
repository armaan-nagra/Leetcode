class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        done = set()

        def dfs(node):
            if node in done:
                return True

            if node in visited:
                return False

            visited.add(node)

            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            
            visited.remove(node)
            done.add(node)
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False 
        
        return True

















