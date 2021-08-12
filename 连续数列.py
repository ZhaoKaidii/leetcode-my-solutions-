class Solution(object):
    def maxSubArray(self, nums):
        dp=[0]+[0]*len(nums)
        for i in range(1,len(nums)+1):
            dp[i]=dp[i-1]*int(dp[i-1]>=0)+nums[i-1]
        del dp[0]
        return max(dp)
