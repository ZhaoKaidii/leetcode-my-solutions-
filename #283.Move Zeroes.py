class Solution(object):
    def moveZeroes(self, nums):
        i,j=0,1
        while j<len(nums) and i<j:
            if nums[i]==0 and nums[j]!=0:
                nums[i]=nums[j]
                nums[j]=0
                i=i+1
                j=j+1
            elif nums[i]==0 and nums[j]==0:
                j=j+1
            else:
                i+=1
                j+=1
        return nums
