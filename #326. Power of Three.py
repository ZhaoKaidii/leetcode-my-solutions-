class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        if n==1:
            return True
        while n>2:
            if n%3!=0:
                return False
            else:
                n=n//3
        return n%3==1
