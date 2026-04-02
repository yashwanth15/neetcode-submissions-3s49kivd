class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited=set()

        def dfs(m,n,i):
            if i==len(word):
                return True
            if (m<0 or m>=rows or
                n<0 or n>=cols or
                board[m][n] != word[i] or 
                (m,n) in visited):
                return False
            visited.add((m,n))
            res = (dfs(m+1,n,i+1) or
                    dfs(m,n+1,i+1) or
                    dfs(m-1,n,i+1) or
                    dfs(m,n-1,i+1))
            visited.remove((m,n))

            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
        