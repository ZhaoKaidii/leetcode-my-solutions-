class Solution(object):
    def monotoneIncreasingDigits(self, N):
        s=[p for p in  str(N)]
        j=1
        while j <len(s):
            if s[j-1]<=s[j]:
                       j=j+1      
            else:
                       s[j-1]=str(int(s[j-1])-1)
                       for y in range(j,len(s)):
                           s[y]=str(9)
                           j=1
        return int(''.join(s))
