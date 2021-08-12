class Solution(object):
    def wordBreak(self, s, wordDict):
        dp=[False]*(len(s)+1)
        dp[0]=True
        s=' '+s
        for i in range(1,len(s)):
            for  j in range(i+1,len(s)+1):
                if dp[i-1] and s[i:j] in wordDict:
                    dp[j-1]=True
        return dp[-1]
