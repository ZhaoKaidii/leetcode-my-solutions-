class Solution(object):
    def removeDuplicates(self, nums):
        i,j=0,1
        while j<len(nums)-1:
            if nums[i]==nums[j+1]:
                del nums[j]
                continue
            i+=1
            j+=1
        return len(nums)
