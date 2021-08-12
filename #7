class Solution:
    def reverse(self, x: int) -> int:
        sign=1 if x>0 else -1
        s=[d for d in str(abs(x))]
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        ans=sign*int("".join(s))
        return ans if ans in range(-2**31,2**31) else 0
