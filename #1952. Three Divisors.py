class Solution(object):
    def isThree(self, n):
        c=1
        for i in range(1,abs(n//2)+1):
            if n%i==0:
                c+=1
            if c>3:
                return False     
        return c==3
