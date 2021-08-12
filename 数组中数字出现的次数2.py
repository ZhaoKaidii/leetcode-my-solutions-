class Solution(object):
    def singleNumber(self, nums):
        a=0
        for i in range(32):
            c=0
            for n in nums:
                f=n>>i
                if f%2!=0:
                    c=c+1
            if c%3!=0:
                a=a+(1<<i)
        return a
