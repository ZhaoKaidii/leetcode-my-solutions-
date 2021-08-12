class Solution(object):
    def maxProduct(self, nums):
        dpmax=[0]*(len(nums))
        dpmin=[0]*(len(nums))
        dpmin[0]=nums[0]
        dpmax[0]=nums[0]
        for i in range(1,len(nums)):
            dpmax[i]=max(nums[i]*dpmax[i-1],nums[i]*dpmin[i-1],nums[i])
            dpmin[i]=min(nums[i]*dpmax[i-1],nums[i]*dpmin[i-1],nums[i])
        return max(dpmax)
