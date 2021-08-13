class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==1:return 1 if nums[0]>=target else 0
        i,j,s,m=0,0,0,float('inf')
        while j<len(nums):
            s+=nums[j]
            while s>=target:
                m=min(m,j-i+1)
                s-=nums[i]
                i+=1   
            j+=1
        return m if m<float('inf') else 0
