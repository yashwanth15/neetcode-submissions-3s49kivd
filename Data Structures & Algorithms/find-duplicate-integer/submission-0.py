class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        freq=[0]*n
        for i in nums:
            freq[i]+=1
        for i,count in enumerate(freq):
            if count>1:
                return i        