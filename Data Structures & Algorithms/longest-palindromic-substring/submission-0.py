class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0
        def palidrome(l,r):
            nonlocal res,reslen
            while (l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
        #odd length
        for i in range(len(s)):
            palidrome(i,i)
        #even ledgth
        for i in range(len(s)):
            palidrome(i,i+1)
        return res

        