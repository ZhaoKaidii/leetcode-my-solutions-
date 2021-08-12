class Solution(object):
    def canBeIncreasing(self, nums):
        if len(nums)==2:
            return True
        c=0
        for i in range(1,len(nums)-1):
            if nums[i]<=nums[i-1]:
                if nums[i-1]<nums[i+1]:
                    del nums[i]
                else:
                    del nums[i-1]
                c+=1
                break
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                if c>0:
                    return False
        return True
