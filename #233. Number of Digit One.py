class Solution(object):
    def countDigitOne(self, n):
        i,counter=1,0
        while i<=n:
            f=10*i
            counter+=(n//f)*i+min(max(n%f-i+1,0),i)
            i=i*10
        return counter
