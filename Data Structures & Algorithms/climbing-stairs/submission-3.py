class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        prev, cur =1,2 #dp[0], dp[1]
        for i in range(2,n):
            prev, cur = cur, cur+prev
        #curr will be dp[n]=dp[n-1]+dp[n-2]
        return cur
        