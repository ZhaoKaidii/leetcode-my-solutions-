class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        ans=i=0
        while i<len(nums)-1:
            ans+=nums[i]
            i+=2
        return ans
