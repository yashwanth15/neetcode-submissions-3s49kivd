class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*m for _ in range(n)]

        def rec(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if i==0 or j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dp[i][j]=rec(i-1,j)+rec(i,j-1)

            return dp[i][j]
        
        return rec(n-1,m-1)
        