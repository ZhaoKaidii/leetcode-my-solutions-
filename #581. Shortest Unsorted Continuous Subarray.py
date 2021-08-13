class Solution(object):
    def findUnsortedSubarray(self, nums):
        nums_sorted=nums[:]
        nums_sorted.sort()
        head,end=0,0
        for i in range(len(nums)):
            if nums[i]!=nums_sorted[i]:
                head=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=nums_sorted[i]:
                end=i
                break
        return end-head+1 if end >0 else 0
