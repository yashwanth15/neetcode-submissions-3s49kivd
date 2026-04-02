class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        res=0

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or grid[r][c]==0:
                return 0
            visited.add((r,c))
            return 1+ dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c]==1:
                    res = max(dfs(r,c),res)
        
        return res



        