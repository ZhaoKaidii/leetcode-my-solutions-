class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a,dic=0,{}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in dic:
            if dic[j]==1:
               a+=j
        return a
