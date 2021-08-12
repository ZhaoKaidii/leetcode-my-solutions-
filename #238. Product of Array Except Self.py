class Solution(object):
    def productExceptSelf(self, nums):
        c,ans=1,[1]*len(nums)
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            c=c*nums[i+1]
            ans[i]=ans[i]*c
        return ans
