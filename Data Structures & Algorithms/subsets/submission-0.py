class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            #exclude nums[i]
            dfs(i+1)
            #include nums[i]
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()

        dfs(0)
        return res
        