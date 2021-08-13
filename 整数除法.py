class Solution:
    def divide(self, a: int, b: int) -> int:
        ans,s=0,True
        if (a>0 and b<0) or (a<0 and b>0):s=False
        a,b=abs(a),abs(b)
        while a>=b:
            i,c=0,b
            while a>=c:
                i,c=i+1,c<<1             
            ans+=2**(i-1)
            a-=(c>>1)
        if s:return ans if ans<2**31-1 else 2**31-1
        else:return -ans if ans>-2**31 else -2**31
