class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h=0
        for i in range(len(citations)):
            if (len(citations)-i)<=citations[i]:
                h=max(h,min(len(citations)-i,citations[i]))
        return h
