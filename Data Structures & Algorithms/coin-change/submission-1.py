class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=[float("inf")]*(amount+1)
        res[0]=0
        for x in range(1,amount+1):
            for c in coins:
                if x-c>=0:
                    res[x] = min(res[x],res[x-c]+1)
        return res[amount] if res[amount]<=amount else -1
        