class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows=len(maze)
        cols=len(maze[0])
        sr,sc=start
        dr,dc=destination
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        q=deque([start])
        visited=set()
        while q:
            r,c=q.popleft()
            if [r,c]==destination:
                return True
            for dr,dc in dir:
                nr,nc=r,c
                while 0<=nr+dr<rows and 0<=nc+dc<cols and maze[nr+dr][nc+dc]==0:
                    nr+=dr
                    nc+=dc
                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append([nr,nc])
        return False
        