class Solution(object):
    def removeDuplicates(self, nums):
        i,j,k=0,1,len(nums)
        while i<len(nums) and j<len(nums):
            if nums[i]==nums[j]:
                del nums[j]
            else:
                i=i+1
                j=j+1
        return len(nums)
