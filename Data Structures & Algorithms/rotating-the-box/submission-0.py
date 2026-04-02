class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # 1) Apply gravity to the right in each row
        for i in range(m):
            write = n-1 # next position to drop a stone
            for j in range(n-1,-1,-1):
                if boxGrid[i][j] == '*':
                    write = j-1 # stones can't cross obstacle
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][write] = '#'
                    write-=1
                # if '.', do nothing

        # 2) Rotate 90 degrees clockwise using a new grid with a formula
        res= [['.']*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m-1-i] = boxGrid[i][j]
        
        return res
        