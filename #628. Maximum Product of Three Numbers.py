class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        i,n=0,len(nums)-1
        c=nums[-1]*nums[n-1]*nums[n-2]
        d=nums[0]*nums[1]*nums[-1]
        return max(c,d)
