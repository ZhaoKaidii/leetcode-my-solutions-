class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2: return True
        if 0 not in nums: return True
        trial=nums[0]
        for  i in range(1,len(nums)-1):
            if i<=trial:
                trial=max(trial,nums[i]+i)
            else:
                break
        return trial>=len(nums)-1
