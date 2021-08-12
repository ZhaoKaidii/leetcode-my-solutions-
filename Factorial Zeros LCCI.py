class Solution(object):
    def trailingZeroes(self, n):
        if n==0:
            return 0
        c=0
        while n>0:
            n=n//5
            c=c+n
        return c
