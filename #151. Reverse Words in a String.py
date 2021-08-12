class Solution:
    def reverseWords(self, s: str) -> str:
        ss=[]
        s=s+" "
        c=d=""
        for i in s:
            if i==" ":
                if c==" " or c=="":
                    continue
                else: 
                    ss.append(c)
                    c=""
            else:
                c=c+i      
        for j in range(len(ss)-1,-1,-1):
            if j==0:
                d=d+ss[j]
            else:
                d=d+ss[j]+" "
        return d
