class Solution(object):
    def nthUglyNumber(self, n):
        i,j,k,dp=0,0,0,[1]*n
        for t in range(1,n):
            dp[t]=min(dp[i]*2,dp[j]*3,dp[k]*5)
            if dp[t]==dp[i]*2:
                i+=1
            if dp[t]==dp[j]*3:
                j+=1
            if dp[t]==dp[k]*5:
                k+=1
        return dp[-1]
