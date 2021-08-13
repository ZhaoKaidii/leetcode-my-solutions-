class Solution(object):
    def repeatedNTimes(self, nums):
        dic={}
        N=len(nums)/2
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            if dic[i]==N:
                return i
