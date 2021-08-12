class Solution(object):
    def findRepeatNumber(self, nums):
        lis=[] 
        for i in range(len(nums)):
            if nums[i] not in lis:
                lis.append(nums[i])
            else:
                return nums[i]
                break
