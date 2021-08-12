class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)<2:
            return len(nums)
        num=[n for n in set(nums)]
        num.sort()
        num=[-float('inf')]+num
        c,d=1,1
        for i in range(1,len(num)):
            if num[i]-num[i-1]==1:
                c+=1
            else:
                c=1
            d=max(d,c)
        return d
