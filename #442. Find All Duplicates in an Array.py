class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic,s={},[]
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]==2:
                s.append(i)
        return s
