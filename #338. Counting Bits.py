class Solution(object):
    def countBits(self, n):
        s=[]
        for i in range(n+1):
            c,k=i,0
            while c>0:
                k=k+c%2
                c>>=1
            s.append(k)
        return s
