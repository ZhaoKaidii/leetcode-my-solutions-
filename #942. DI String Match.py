class Solution(object):
    def diStringMatch(self, s):
        small,large=0,len(s)
        f=[]
        for i in range(len(s)):
            if s[i]=="I":
                f.append(small)
                small+=1
            else:
                f.append(large)
                large-=1
        f.append(large)
        return f
