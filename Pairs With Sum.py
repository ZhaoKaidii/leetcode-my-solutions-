class Solution(object):
    def pairSums(self, nums, target):
        s=[]
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]+nums[j]<target:
                i+=1
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                s.append([nums[i],nums[j]])
                i+=1
                j-=1
        return s
