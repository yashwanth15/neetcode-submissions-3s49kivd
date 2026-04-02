class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        n=len(s)

        lens=set(len(w) for w in wordSet) #lengths of all words
        dp=[False]*(n+1)
        dp[0]=True # empty string is “segmentable”

        for i in range(1,n+1):
            for L in lens:
                if i-L>=0 and dp[i-L] and s[i-L:i] in wordSet:
                    dp[i]=True
                    break
        return dp[n]
        