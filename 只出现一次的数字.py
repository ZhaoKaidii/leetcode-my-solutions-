class Solution(object):
    def singleNumber(self, nums):
        s,f=sum(nums),sum(set(nums))
        return s-(s-f)*3/2
