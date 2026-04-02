class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        # lower bound
        while l<r:
            m = (l+r)//2
            # find and eliminate sorted half
            if nums[m]<=nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]
            