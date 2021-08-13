class Solution(object):
    def findContentChildren(self, g, s):
        s.sort(reverse=True)
        g.sort(reverse=True)
        i,j,ans=0,0,0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                ans+=1
                i+=1
                j+=1
            else:
                j+=1
        return ans
