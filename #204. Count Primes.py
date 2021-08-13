class Solution(object):
    def countPrimes(self, n):
        d=[True]*n
        ans=0
        for i in range(2,n):
            if d[i]:
                ans+=1
                for k in range(1,(n-1)//i+1):
                    d[k*i]=False
        return ans
