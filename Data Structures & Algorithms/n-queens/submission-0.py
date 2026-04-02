class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        ans=[]
        cols=set()
        rightdiag=set()
        leftdiag=set()

        def dfs(r):
            if r==n:
                copy=["".join(row) for row in board]
                ans.append(copy)
                return
            for c in range(n):
                if c in cols or r+c in rightdiag or r-c in leftdiag:
                    continue
                cols.add(c)
                rightdiag.add(r+c)
                leftdiag.add(r-c)
                board[r][c]="Q"
                dfs(r+1)
                cols.remove(c)
                rightdiag.remove(r+c)
                leftdiag.remove(r-c)
                board[r][c]="."

        dfs(0)
        return ans
        