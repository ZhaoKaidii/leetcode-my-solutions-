class Solution(object):
    def majorityElement(self, nums):
        s=collections.Counter(nums)
        c=-1
        for n in nums:
            if s[n]>len(nums)/2:
                return n
        return c
