class Solution(object):
    def guessNumber(self, n):
        a,b=1,n
        while a<=b:
            mid=(a+b)//2
            if guess(mid)<0:
                b=mid
            elif guess(mid)>0:
                a=mid+1
            else:
                return mid
