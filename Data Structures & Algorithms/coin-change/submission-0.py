class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=[float("inf")]*(amount+1)
        res[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if c>i:
                    continue
                res[i]=min(res[i],1+res[i-c])
        return res[amount] if res[amount]<=amount else -1
        