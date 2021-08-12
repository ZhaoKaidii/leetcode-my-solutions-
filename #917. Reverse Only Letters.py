class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ss=[c for c in s]
        i,j=0,len(ss)-1
        while i<j:
            if not (ss[j].isalpha()):
                j-=1
            elif not (ss[i].isalpha()):
                i+=1
            else:
                a=ss[i]
                b=ss[j]
                ss[i]=b
                ss[j]=a
                i=i+1
                j=j-1
        return "".join(ss)
