class Solution(object):
    def subarraySum(self, nums, k):
        dic={0:1} 
        ans=summation=0
        for i in nums:
            summation+=i
            ans+=dic.get(summation-k,0)
            if summation in dic:
                dic[summation]+=1
            else:
                dic[summation]=1
        return ans
