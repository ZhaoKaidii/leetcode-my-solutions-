class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return True
        c=True&(n>0)
        while n >1:
            c=c&(n%4==0)
            n>>=2
        return c
