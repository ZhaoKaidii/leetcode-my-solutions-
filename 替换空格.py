class Solution(object):
    def replaceSpace(self, s):
        ss=[c for c in s]
        for i in range(len(ss)):
            if ss[i]==' ':
                ss[i]='%20'
        return ''.join(ss)
