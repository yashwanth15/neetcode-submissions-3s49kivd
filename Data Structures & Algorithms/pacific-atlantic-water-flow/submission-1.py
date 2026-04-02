class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac = [ [False]*cols for _ in range(rows)]
        atl = [ [False]*cols for _ in range(rows)]
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        res=[]

        def dfs(r,c,seen):
            seen[r][c]=True
            for dr,dc in dirs:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and not seen[nr][nc]:
                    if heights[r][c]<=heights[nr][nc]:
                        dfs(nr,nc,seen)

        
        #top
        for c in range(cols):
            dfs(0,c,pac)
        #left
        for r in range(rows):
            dfs(r,0,pac)

        #bottom
        for c in range(cols):
            dfs(rows-1,c,atl)
        #right
        for r in range(rows):
            dfs(r,cols-1,atl)
        
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res

        