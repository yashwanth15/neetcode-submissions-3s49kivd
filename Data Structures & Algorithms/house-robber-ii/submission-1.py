class Solution:
    def rob(self, nums: List[int]) -> int:
        #skip the first house or skip the last house entirely and find the max
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr
        return prev1
        