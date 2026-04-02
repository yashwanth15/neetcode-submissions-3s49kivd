class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        n=len(nums)
        picked=[False]*n
        def dfs():
            if len(perm) == n:
                res.append(perm.copy())
                return
            for j in range(n):
                if not picked[j]:
                    picked[j]=True
                    perm.append(nums[j])
                    dfs()
                    perm.pop()
                    picked[j]=False

        dfs()
        return res
        