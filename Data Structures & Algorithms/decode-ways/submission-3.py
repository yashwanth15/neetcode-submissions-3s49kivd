class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0

        dp1=1
        dp2=0

        #bottomup approach
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                cur=0
            else:
                cur=dp1

                if (i+1<n and '10'<=s[i:i+2]<='26'):
                    cur+=dp2
            dp2=dp1
            dp1=cur
        return dp1