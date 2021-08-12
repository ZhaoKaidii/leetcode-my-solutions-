class Solution(object):
    def maxSubArray(self, nums):
        s=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            s[i]=int(s[i-1]>=0)*s[i-1]+nums[i-1]
        del s[0]
        return max(s)
