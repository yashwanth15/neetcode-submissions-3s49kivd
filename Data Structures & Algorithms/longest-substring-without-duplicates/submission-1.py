class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,res=0,0,0
        seq=set()
        while r<len(s):
            if s[r] not in seq:
                seq.add(s[r])
                res=max(res,len(seq))
                r+=1
            else:
                seq.remove(s[l])
                l+=1
        return res
