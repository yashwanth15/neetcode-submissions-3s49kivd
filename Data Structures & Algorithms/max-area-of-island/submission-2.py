class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        res=0

        #bfs
        def bfs(r,c):
            area=1
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col = q.popleft()
                for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                    i=row+dr
                    j=col+dc
                    if (i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]==0):
                        continue
                    q.append((i,j))
                    area+=1
                    visited.add((i,j))
            return area

        
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c]==1:
                    res = max(bfs(r,c),res)
        
        return res



        