class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(s):
            i,j=0,len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True       
        i,j=0,len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return isPalindrome(s[i:j])|isPalindrome(s[i+1:j+1])
        return True
