class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque() # rotten oranges
        fresh=0 # oranges

        # multi-source bfs
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        minutes=0
        while fresh>0 and q:
            for _ in range(len(q)):
                pr,pc = q.popleft()
                for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                    r=dr+pr
                    c=dc+pc
                    if 0<=r<m and 0<=c<n and grid[r][c]==1:
                        grid[r][c]=2
                        q.append((r,c))
                        fresh-=1
            minutes+=1
        
        return minutes if fresh==0 else -1 #subtract the extra level

        