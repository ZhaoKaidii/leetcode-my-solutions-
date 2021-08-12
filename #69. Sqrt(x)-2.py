class Solution(object):
    def mySqrt(self, x):
        a,b=1,(x//2)+1
        while a<b:
            s=(a+b)//2
            if s**2>=x:
                b=s
            else:
                a=s+1
        return a if a**2<=x else a-1        
