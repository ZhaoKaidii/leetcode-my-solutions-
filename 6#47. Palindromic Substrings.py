class Solution:
    def countSubstrings(self, s: str) -> int:
        ss=[]
        lis=['']
        for i in range(len(s)):
            lis.append(s[i])
            lis.append('')
        for j in range(1,len(lis)-1):
            c=lis[j]
            tt=min(j,len(lis)-j-1)
            for t in range(1,tt):
                if lis[j-t]==lis[j+t]:
                    c=lis[j-t]+c+lis[j-t]
                    ss.append(c)
                else:
                    ss.append(c)
                    break
        return len(ss)
