class Solution(object):
    def maxAscendingSum(self, nums):
        if len(nums)<2:
            return nums[0]
        c=d=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=nums[i]
                d=max(d,c)
            else:
                c=nums[i]
                d=max(d,c)
        return d
