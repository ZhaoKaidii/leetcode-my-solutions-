class Solution:
    def numSquares(self, n: int) -> int:
        sqrt=int(n**0.5)
        coins=[n**2 for n in range(1,sqrt+1)]
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,n+1):
                dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1]
