class Solution:
    def rob(self, nums: List[int]) -> int:
        #skip the first house or skip the last house entirely and find the max
        #if len(nums) is 1 then nums[0] would be our answer
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        lastbutone, previous = 0, 0
        # lastbutone = dp[i-2], previous = dp[i-1]
        # [lastbutone, previous, n, n+2,..]
        for amount in nums:
            # If we rob this house, total = lastbutone + amount
            # If we skip, total = previous
            curr = max(previous, lastbutone + amount)
            lastbutone = previous
            previous = curr
        return previous
        