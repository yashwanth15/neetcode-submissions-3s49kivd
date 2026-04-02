class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        INF=2147483647
        
        # start from treasure nodes to keep the time & space complexity at O(mn)
        # use multisource bfs to start from treasure nodes first. This ensures that first visit has the least distance
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        
        while q:
            row,col = q.popleft()
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                r=row+dr
                c=col+dc
                if 0<=r<m and 0<=c<n and grid[r][c]==INF:
                    grid[r][c] = grid[row][col]+1
                    q.append((r,c))
        # Water (-1) cells and treasures (0) remain unchanged
        