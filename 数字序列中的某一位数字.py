class Solution(object):
    def findNthDigit(self, n):
        dig,count,start=1,9,1
        while n>count:
            n-=count
            start*=10
            dig+=1
            count=9*dig*start
        num=start+(n-1)//dig 
        return int(str(num)[(n-1)%dig]) 
