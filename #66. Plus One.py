class Solution(object):
    def plusOne(self, digits):
        k=1
        for i in range(len(digits)-1,-1,-1):
            if k==1:
                digits[i]=digits[i]+1
                k=digits[i]//10
                digits[i]=digits[i]%10
            else:
                break
        if k==1:
            digits=[1]+digits
        return digits
