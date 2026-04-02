class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*n
        def rec(i):
            if i==0 or i==1:
                return cost[i]
            if dp[i]!=-1:
                return dp[i]
            dp[i]=cost[i]+min(rec(i-1),rec(i-2))
            return dp[i]
        
        return min(rec(n-1),rec(n-2))
        