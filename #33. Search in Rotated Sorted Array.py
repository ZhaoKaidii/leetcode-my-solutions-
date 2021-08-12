class Solution(object):
    def search(self, nums, target):
        nums=nums+[float('inf')]
        if nums[0]>target:
            i=len(nums)-2
            while nums[i]<nums[i+1]:
                if nums[i]==target:
                    return i
                i-=1
        else:
            nums=[-1]+nums
            i=1
            while i<len(nums) and nums[i-1]<nums[i]:
                if nums[i]==target:
                    return i-1
                i+=1
        return -1
