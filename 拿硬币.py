class Solution(object):
    def minCount(self, coins):
        c=0
        for i in range(len(coins)):
            while coins[i] >0:
                c=c+1
                coins[i]-=2
        return c
