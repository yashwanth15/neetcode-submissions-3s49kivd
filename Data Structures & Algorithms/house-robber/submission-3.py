class Solution:
    def rob(self, nums: List[int]) -> int:
        lastbutone, previous = 0, 0
        # lastbutone = dp[i-2], previous = dp[i-1]
        for amount in nums:
            # If we rob this house, total = lastbutone + amount
            # If we skip, total = previous
            curr = max(previous, lastbutone + amount)
            lastbutone = previous
            previous = curr
        return previous
        