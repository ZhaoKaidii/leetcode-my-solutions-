class Solution(object):
    def isStraight(self, nums):
        nums.sort()
        s=collections.Counter(nums)[0]
        d=[True]*2+[False]*(len(nums)-1)
        for i in range(2,len(nums)+1):
            d[i]=(d[i-1] and (((nums[i-1]-nums[i-2]-1)<=s) and s>=0)) or nums[i-2]==0
            s=s-(nums[i-1]-nums[i-2]-1)*int(nums[i-1]*nums[i-2]!=0)
            if nums[i-1]==nums[i-2] and nums[i-1]*nums[i-2]!=0:
                return False
        return d[-1]
