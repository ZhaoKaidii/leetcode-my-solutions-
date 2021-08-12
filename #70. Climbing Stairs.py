class Solution(object):
    def climbStairs(self, n):
        k=[0]+[1]+[0]*n
        for i in range(2,n+2):
                k[i]+=k[i-1]+k[i-2]
        return k[-1]
