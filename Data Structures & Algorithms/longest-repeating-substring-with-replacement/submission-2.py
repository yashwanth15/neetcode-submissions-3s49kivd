class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        l,r,res=0,0,0
        while r<len(s):
            count[s[r]]+=1
            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res
        