class Solution(object):
    def waysToStep(self, n):
        a,b,c=0,0,1
        for i in range(n):
            g=(a+b+c)%1000000007
            a=b
            b=c
            c=g
        return g%1000000007
