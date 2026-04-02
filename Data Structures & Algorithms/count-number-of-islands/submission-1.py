class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=[[False]*cols for _ in range(rows)]
        islands=0

        def bfs(r,c):
            q=deque()
            visited[r][c]=True
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if (r<0 or c<0 or
                    r>=rows or c>=cols or 
                    visited[r][c] or grid[r][c]=="0"):
                        continue
                    visited[r][c]=True
                    q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]=="1":
                    islands+=1
                    bfs(r,c)
        return islands
        