class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while (l<=r):
            m = (l+r)//2
            if target==nums[m]:
                return m

            # first detect which half is sorted and check if target lies in that range else discard that half.
            # let's check if left half is sorted
            if (nums[l]<=nums[m]):
                # left half is sorted.
                # now check if targrt lies here
                if (nums[l]<=target<=nums[m]):
                    r=m-1
                else:
                    l=m+1
            else:
                # right half is sorted.
                # check if target lies here
                if (nums[m]<=target<=nums[r]):
                    l=m+1
                else:
                    r=m-1
        return -1
        
        