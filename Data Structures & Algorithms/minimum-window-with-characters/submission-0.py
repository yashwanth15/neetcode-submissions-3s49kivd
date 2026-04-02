class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        tcount={}
        for char in t:
            tcount[char]=1+tcount.get(char,0)
        window={}
        have,need=0,len(tcount)
        res=[-1,-1]
        resLen=float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in tcount and window[c]==tcount[c]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in tcount and window[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float("infinity") else ""
            

        