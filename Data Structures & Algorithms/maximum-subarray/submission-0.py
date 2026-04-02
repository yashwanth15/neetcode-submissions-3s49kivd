class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        cur=0
        for n in nums:
            cur+=n
            res=max(cur,res)
            if cur<0:
                cur=0
        return res
        