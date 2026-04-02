class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        need=Counter(t)
        window=Counter()
        matches=0 #stores the number of charactes whose freq is equal in the counters.
        l=0
        resultindices=[-1,-1]
        resultlen=float("inf")
        for r in range(len(s)):
            right=s[r]
            window[right]+=1
            if right in need and window[right] == need[right]:
                matches+=1
            
            # we have found a substring, now shrick till we find the minimum substring
            while matches==len(need):
                if (r-l+1)<resultlen:
                    resultindices=[l,r]
                    resultlen=r-l+1
                left=s[l]
                window[left]-=1
                if left in need and window[left] < need[left]:
                    matches-=1
                l+=1
        l,r=resultindices
        return s[l:r+1]
        