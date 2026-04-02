class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        perm=[]
        def dfs(start,end):
            if len(perm)==2*n:
                res.append("".join(perm))
                return
            if start<n:
                perm.append("(")
                dfs(start+1,end)
                perm.pop()
            if end<start:
                perm.append(")")
                dfs(start,end+1)
                perm.pop()

        dfs(0,0)
        return res
        