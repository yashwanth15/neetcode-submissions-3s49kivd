class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2=0,0
        for n in nums:
            cur=max(rob1+n,rob2)
            rob1=rob2
            rob2=cur
        return rob2
        