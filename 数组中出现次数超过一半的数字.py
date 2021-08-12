class Solution(object):
    def majorityElement(self, nums):
        import collections
        c=collections.Counter(nums)
        m=len(nums)/2
        for y in nums:
            if c[y]>=m:                                                   
                    return y
