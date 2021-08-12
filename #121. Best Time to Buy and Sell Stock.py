class Solution(object):
    def maxProfit(self, prices):
        a,b=prices[0],0
        for i in range(len(prices)):
            a=min(a,prices[i])
            b=max(b,prices[i]-a)
        return b
