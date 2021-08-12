class Solution(object):
    def maxSubArray(self, nums):
        ss=[]
        ss.append(nums[0])
        for i in range(1,len(nums)):
            c=int(ss[-1]>=0)*ss[-1]+nums[i]
            ss.append(c)
        return max(ss)
