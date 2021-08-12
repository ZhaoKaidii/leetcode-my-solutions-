class Solution(object):
    def longestPalindrome(self, s):
        ss=[s[0]]
        lis=['']
        for l in range(len(s)):
            lis.append(s[l])
            lis.append('')
        for i in range(1,len(lis)-1): 
            c=lis[i] 
            t=min(i,len(lis)-i-1)
            for j in range(1,t): 
                if lis[i+j]==lis[i-j]:
                    c=lis[i-j]+c+lis[i+j]
                    if len(c)>len(ss[-1]):
                            ss.pop()
                            ss.append(c)
                else:
                    i=i+j
                    break  
        return ''.join(ss[-1])
