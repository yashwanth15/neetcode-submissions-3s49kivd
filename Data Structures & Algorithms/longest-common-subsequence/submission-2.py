class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        memo={}

        def rec(i,j):
            if i <0 or j<0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i]==text2[j]:
                memo[(i,j)] = 1+rec(i-1,j-1)
            else:
                memo[(i,j)] = max(rec(i-1,j),rec(i,j-1))
            return memo[(i,j)]
        
        return rec(n-1,m-1)
        