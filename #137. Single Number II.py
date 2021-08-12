class Solution(object):
    def singleNumber(self, nums):
        s=sum(nums)
        d=set(nums)
        return s-3*(s-sum(d))/2
