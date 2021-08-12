class Solution:
    def largestOddNumber(self, num: str) -> str:
        c=0
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                c=i+1
                break
        return num[:c]
