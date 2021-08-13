class Solution(object):
    def addBinary(self, a, b):
        d,p,ans=len(b)-len(a),0,""
        a="0"*d+a
        b="0"*(-d)+b 
        for i in range(len(a)-1,-1,-1):
            g=int(a[i])+int(b[i])+p
            ans=str(g%2)+ans
            p=g//2
        return ans if p==0 else "1"+ans
