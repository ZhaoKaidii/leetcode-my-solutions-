class Solution(object):
    def myPow(self, x, n):
        c=1
        if n<0:
            x,n=1/x,-n
        while n:
            if n&1:
                c=c*x
            x*=x
            n>>=1
        return c
