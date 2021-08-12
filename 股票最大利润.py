class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        c=float('inf')
        dp=[0]*len(prices)
        for i in range(len(prices)):
            c=min(c,prices[i])
            dp[i]=prices[i]-c
        return max(dp)
