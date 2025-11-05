class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #dfs approach? create an array of arrays of size m x n 
        grid = []
        rows, cols = m, n
        for r in range(rows):
            grid.append([])
            for c in range(cols):
                grid[r].append('c')
        
        for x, y in guards:
            grid[x][y] = 'g'
        
        for x, y in walls:
            grid[x][y] = 'w'

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for gx, gy in guards:
            for dx, dy in directions:
                x, y = gx + dx, gy + dy

                while 0 <= x < rows and 0 <= y < cols and grid[x][y] not in ('w', 'g'):
                    if grid[x][y] == 'c':
                        grid[x][y] = 'v'
                    x += dx 
                    y += dy
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'c':
                    res += 1
        return res

