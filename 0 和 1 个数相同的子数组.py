class Solution(object):
    def findMaxLength(self, nums):
        dic={0:-1}
        ans,count=0,0
        for i,num in enumerate(nums):
            if num==1:
                count+=1
            else:
                count-=1
            if count in dic:
                ans=max(ans,i-dic[count])
            else:
                dic[count]=i
        return ans
