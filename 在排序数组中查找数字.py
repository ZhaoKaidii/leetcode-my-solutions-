class Solution(object):
    def search(self, nums, target):
        if len(nums)<2:
            return len(nums)*int( target in nums)
        else:
            i,j=0,len(nums)-1
            while i<j:
                if (target>nums[i]) or (target<nums[j]):
                    i=i+int(target>nums[i])          
                    j=j-int(target<nums[j])
                else:    
                    break
            return (j-i+1)*int(target in nums)
