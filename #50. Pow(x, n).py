class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        if x==0 or x==1:
            return x
        if n<0:
            x,n=1/x,-n
        c=1
        while n:
            if n%2:
                c*=x
            x*=x
            n//=2
        return c
