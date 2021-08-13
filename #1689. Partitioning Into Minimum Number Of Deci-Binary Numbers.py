class Solution(object):
    def minPartitions(self, n):
        c=0
        for i in n:
            c=max(c,int(i)) 
        return c
