class Solution:
    def reverseString(self, s: List[str]) -> None:
        i,j=0,len(s)-1
        while i<j:
            a=s[i]
            s[i]=s[j]
            s[j]=a
            i+=1
            j-=1
        return s
