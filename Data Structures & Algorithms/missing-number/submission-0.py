class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        n=len(nums)
        formula=(n*(n+1))//2
        return formula-total