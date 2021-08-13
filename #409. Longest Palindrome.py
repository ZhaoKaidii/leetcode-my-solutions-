class Solution(object):
    def longestPalindrome(self, s):
        dic=collections.Counter(s)
        b=c=0
        for i in dic:
            b+=dic[i]
            if dic[i]%2==1:
                c+=1
        return b-c+1 if c>0 else b
