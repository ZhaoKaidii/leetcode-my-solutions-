class Solution(object):
    def hammingWeight(self, n):
        c=0
        while n>0:
            c=c+n%2
            n>>=1
        return c
