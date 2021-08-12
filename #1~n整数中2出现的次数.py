class Solution(object):
    def numberOf2sInRange(self, n):
        i,counter=2,0
        while i<=n:
            d,div=i/2,5*i
            counter+=(n//div)*d+min(max(n%div-i+1,0),d)
            i=i*10
        return c
