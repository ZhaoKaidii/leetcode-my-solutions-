class Solution(object):
    def trailingZeroes(self, n):
        c=0
        while n>0:
            n=n//5
            c=c+n
        return c
