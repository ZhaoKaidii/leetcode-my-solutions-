class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1,-1]
        elif len(nums)==1:
           return [0,0]
        else:
            i,j=0,len(nums)-1
            while i<j:
                if (target>nums[i]) or (target<nums[j]):
                    i=i+int(target>nums[i])          
                    j=j-int(target<nums[j])
                else:    
                    break
            return [i,j]
