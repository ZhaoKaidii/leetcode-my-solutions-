class Solution(object):
    def nextPermutation(self, nums):
        i=len(nums)-1
        while i>0:
            if nums[i-1]<nums[i]:
                a,j=i-1,len(nums)-1
                while a<j:
                    if nums[j]>nums[a]:
                        nums[j],nums[a]=nums[a],nums[j]
                        f=len(nums)-1
                        while (a+1)<f:
                            nums[a+1],nums[f]=nums[f],nums[a+1]
                            a+=1
                            f-=1
                        return nums
                    j-=1
            i-=1
        nums.sort()
        return nums
