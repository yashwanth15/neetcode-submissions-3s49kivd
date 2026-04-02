class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in myMap:
                return [myMap[complement],i]
            myMap[num]=i
        return [0,0]