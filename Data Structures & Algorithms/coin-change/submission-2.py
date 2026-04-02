class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}

        def rec(target):
            if target==0:
                return 0
            if target<0:
                return float("inf")
            if target in dp:
                return dp[target]
            
            best=float("inf")
            for coin in coins:
                if target>=coin:
                    best = min(best, 1+rec(target-coin))
            dp[target]=best
            return dp[target]
        res=rec(amount)
        return res if res!=float("inf") else -1
        