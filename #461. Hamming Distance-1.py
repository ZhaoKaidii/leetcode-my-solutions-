class Solution:
    def hammingDistance(self, x, y):
        c=x^y
        ans=0
        while c>0:
            ans+=c%2
            c>>=1
        return ans
