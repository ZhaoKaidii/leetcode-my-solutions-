class Solution(object):
    def search(self, nums, target):
        n=int(len(nums)/2)
        if nums[n]==target:
            return n
        if nums[n]<target:
            for i in range(n+1,len(nums)):
                if nums[i]==target:
                    return i
        if nums[n]>target:
            for i in range(n):
                if nums[i]==target:
                    return i
        return -1
