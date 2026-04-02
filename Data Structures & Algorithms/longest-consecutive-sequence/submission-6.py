class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        unique=set(nums)
        res=1
        for num in unique:
            if num-1 not in unique:
                count=1
                while num+count in unique:
                    count+=1
                res=max(res,count)
        return res
        