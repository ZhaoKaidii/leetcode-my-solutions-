class Solution(object):
    def judgeSquareSum(self, c):
        h=int(c**0.5)+1
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
