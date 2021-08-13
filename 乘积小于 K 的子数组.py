class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k<=1:return 0
        i,j,s,ans=0,0,1,0
        while j<len(nums):
            s*=nums[j]
            while s>=k:
                s,i=s/nums[i],i+1
            ans,j=ans+(j-i+1),j+1        
        return ans
