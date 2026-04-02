class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        prev=cost[0]
        cur=cost[1]
        for i in range(2,n):
            prev,cur=cur,cost[i]+min(prev,cur)
        
        return min(prev,cur)
        