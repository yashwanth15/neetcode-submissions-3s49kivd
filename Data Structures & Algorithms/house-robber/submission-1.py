class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        # prev2 = dp[i-2], prev1 = dp[i-1]
        for amount in nums:
            # If we rob this house, total = prev2 + amount
            # If we skip, total = prev1
            curr = max(prev1, prev2 + amount)
            prev2, prev1 = prev1, curr
        return prev1
        