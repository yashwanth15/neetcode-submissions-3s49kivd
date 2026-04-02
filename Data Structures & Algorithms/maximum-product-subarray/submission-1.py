class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin,curMax=1,1
        for n in nums:
            if n==0:
                curMin,curMax=1,1
                continue
            prevMax=curMax
            curMax=max(n*prevMax,n*curMin,n)
            curMin=min(n*prevMax,n*curMin,n)
            res=max(res,curMax)
        return res

        