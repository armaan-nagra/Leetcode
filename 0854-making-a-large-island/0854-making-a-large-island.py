class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)


        def out_of_bounds(r, c):
            return (r < 0 or c < 0 or r >= n or c >= n)

        def dfs(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] == 0 or grid[r][c] == label:
                return 0
            
            grid[r][c] = label
            size = 1 
            nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]

            for nr, nc in nei:
                size += dfs(nr,nc,label)
            
            return size

        #precompute areas
        size = defaultdict(int) #island id -> area
        label = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1
        

        def connect(r, c):
            nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            visit = set()
            res = 1
            for nr, nc in nei:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                    res += size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res
            
        res = 0 if not size else max(size.values())
        #try flipping every water cell
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    res = max(connect(r, c), res)
            
        return res

        























        # rows, cols = len(grid), len(grid[0])
        # res = 0
        # #try brute force way, where you flip current value if 0 to a 1 and then DFS
        # visited = set()
        # def dfs(r, c, length):
        #     if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
        #         return 0

        #     visited.add((r,c))
        #     total = 0
        #     total += dfs(r, c+1, length)
        #     total += dfs(r, c-1, length)
        #     total += dfs(r+1, c, length)
        #     total += dfs(r-1, c, length)
        #     return 1 + total

        # has_zero = False
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 0:
        #             has_zero = True
        #             grid[r][c] = 1
        #             res = max(dfs(r,c,0), res)
        #             grid[r][c] = 0
        #         visited.clear()
        
        # if has_zero:
        #     return res
        # else:
        #     return rows*cols