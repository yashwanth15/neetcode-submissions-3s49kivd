class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        buy=prices[0]
        for price in prices:
            res=max(res,price-buy)
            buy=min(buy,price)
        return res