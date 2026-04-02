class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Flip the thinking: Any O connected to the border cannot be captured. Everything else can.
        #1. Find all Os on the border and mark them safe (DFS/BFS from border)
        #2. Everything else that's O gets flipped to X

        rows=len(board)
        cols=len(board[0])

        def dfs(r,c):
            if 0<=r<rows and 0<=c<cols and board[r][c]=="O":
                board[r][c]="S"
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)
        
        # Find all Os on the boarder and mark them safe (DFS from border)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r==0 or r==rows-1 or c==0 or c==cols-1):
                    dfs(r,c)
        
        # Everything else that's O gets flipped to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="S":
                    board[r][c]="O"
        
        