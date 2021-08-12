class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        h=int(c**0.5)+1
        if c**0.5-h==0:
            return True
        s=[n**2 for n in range(h)]
        i,j=0,len(s)-1
        while i<=j:
            if s[i]+s[j]==c:
                return True
            elif s[i]+s[j]>c:
                j=j-1
            else:
                i=i+1
        return False
