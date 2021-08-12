class Solution(object):
    def cuttingRope(self, n):
        if n<4:
            return int(n/2)*(n-int(n/2))
        f=0
        for i in range(2,int(n/2)+1):
            c=max((n%i)*(i**(n//i)),(i+n%i)*(i**((n//i)-1)))
            f=max(c,f)
        return f
