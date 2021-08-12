class Solution(object):
    def twoSum(self, nums, target):
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]+nums[j]>target:
                j=j-1
            elif nums[i]+nums[j]<target:
                i=i+1
            else:
                return [nums[i],nums[j]]
                break
