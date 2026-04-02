import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows=len(maze)
        cols=len(maze[0])
        sr,sc=start
        rr,rc=destination
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[[float("inf")]*cols for _ in range(rows)]
        q=[(0,sr,sc)]
        while q:
            dist,r,c=heapq.heappop(q)
            if [r,c]==destination:
                return dist
            for dr,dc in dir:
                nr=r
                nc=c
                steps=0
                while 0<=nr+dr<rows and 0<=nc+dc<cols and maze[nr+dr][nc+dc]==0:
                    nr+=dr
                    nc+=dc
                    steps+=1
                new_dist=steps+dist
                if new_dist<res[nr][nc]:
                    res[nr][nc]=new_dist
                    heapq.heappush(q,(new_dist,nr,nc))
        return -1 if res[rr][rc]==float("inf") else res[rr][rc]
