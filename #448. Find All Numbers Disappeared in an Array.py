class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic=collections.Counter(nums)
        s=[]
        for i in range(1,len(nums)+1):
            if dic.get(i,0)==0:
                s.append(i)
        return s
