class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        i,j,d,dp=0,0,0,[1]*k 
        for t in range(1,k):
            dp[t]=min(dp[i]*3,dp[j]*5,dp[d]*7)
            if dp[t]==dp[i]*3:
                i+=1
            if dp[t]==dp[j]*5:
                j+=1
            if dp[t]==dp[d]*7:
                d+=1
        return dp[k-1]
