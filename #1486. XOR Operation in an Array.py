class Solution(object):
    def xorOperation(self, n, start):
        nums=[(start+2*i) for i in range(0,n)]
        SS=nums[0]
        for i in range(1,len(nums)):
            SS=SS^nums[i]
        return SS
