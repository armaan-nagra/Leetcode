class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = [[False] * cols for _ in range(rows)]


        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 1
            
            if grid[row][col] == 0:
                return 1
            
            if visited[row][col]:
                return 0

            visited[row][col] = True
            
            return (
                dfs(row, col + 1) +
                dfs(row, col - 1) + 
                dfs(row + 1, col) + 
                dfs(row - 1, col)
            )

        


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)
        
        return 0


        