class Solution(object):
    def waysToChange(self, n):
        mod=1000000007
        c=[1,5,10,25]
        k=[0]*(n+1)
        k[0]=1
        for cc in c:
            for i in range(cc,n+1):
                k[i]=k[i]+k[i-cc]
        return k[-1]%mod  
