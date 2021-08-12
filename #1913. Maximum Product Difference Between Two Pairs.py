class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        a,b,c,d=nums[0],nums[1],nums[len(nums)-2],nums[len(nums)-1]
        return c*d-a*b
