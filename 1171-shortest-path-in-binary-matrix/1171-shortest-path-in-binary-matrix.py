class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #bfs? and if you reach it, return the length?
        n = len(grid)
        q = deque()
        if grid[0][0] == 0:
            q.append([(0,0), 1])
        else:
            return -1
        vectors = [[0,1], [1,0], [0,-1], [-1,0], [-1,-1], [1,1], [1,-1], [-1,1]]
        visited = set()
        visited.add((0,0))
        while q:
            qLen = len(q)

            for i in range(qLen):
                (x, y), length = q.popleft()
                if x == n - 1 and y == n - 1:
                    return length 
                for ax, ay in vectors:
                    nx, ny = ax + x, ay + y
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or grid[nx][ny] == 1 or (nx, ny) in visited:
                        continue
                    visited.add((nx,ny))
                    q.append([(nx,ny), length + 1])
        
        return -1
        