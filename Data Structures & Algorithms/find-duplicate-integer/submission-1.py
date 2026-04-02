class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique=set()
        for i in nums:
            if i in unique:
                return i
            unique.add(i)       