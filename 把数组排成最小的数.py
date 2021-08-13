class Solution:
    def minNumber(self, nums: List[int]) -> str:
        num=[str(c) for c  in nums]
        if len(num)<2:
            return num[0]
        for i in range(len(num)-1):
            j=i+1
            while j<len(num):
                if num[i]+num[j]>num[j]+num[i]:
                    num[i],num[j]=num[j],num[i]
                j+=1
        return "".join(num)
