class Solution(object):
    def findMin(self, nums):
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[right]>nums[mid]:
                right=mid
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right-=1
        return nums[left]
