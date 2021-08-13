class Solution(object):
    def largestNumber(self, nums):
        num=[str(c) for c  in nums]
        if len(num)<2:
            return num[0]
        for  i in range(len(num)-1):
            j=i+1
            while j<len(nums):
                if num[i]+num[j]<num[j]+num[i]:
                    num[i],num[j]=num[j],num[i]
                j+=1
        k=0
        while k<len(num)-1:
            if num[k]!="0":
                break
            else:
                k+=1
        return "".join(num[k:])
