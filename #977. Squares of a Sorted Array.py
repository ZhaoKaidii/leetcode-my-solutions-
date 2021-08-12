class Solution(object):
    def sortedSquares(self, nums):
        nums.sort(key=lambda x:abs(x))
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        return nums
