class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        picked=[False]*n
        def dfs(i,perm,picked):
            if len(perm) == n:
                res.append(perm.copy())
            if i>=n:
                return
            for j in range(n):
                if not picked[j]:
                    picked[j]=True
                    perm.append(nums[j])
                    dfs(j,perm,picked)
                    perm.pop()
                    picked[j]=False

        for i in range(n):
            picked[i]=True
            dfs(i,[nums[i]],picked)
            picked[i]=False
        return res
        