class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        else:
            a=int(math.exp(math.log(x)/2))
            c=(a+1)**2>x
            return a*int(c)+(a+1)*int(not c)
