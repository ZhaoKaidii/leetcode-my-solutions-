class Solution:
    def countSubstrings(self, s: str) -> int:
        lis,y=[""],len(s)
        for l in s:
            lis.append(l)
            lis.append("")
        for i in range(1,len(lis)-1):
            for j in range(1,len(lis)-i-1):
                if (lis[i+j]==lis[i-j]) and lis[i+j]!='':
                    y=y+1
                elif (lis[i+j]==lis[i-j]) and lis[i+j]=='':
                    continue
                else:
                    break  
        return y
