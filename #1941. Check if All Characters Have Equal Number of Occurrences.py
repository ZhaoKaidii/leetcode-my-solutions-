class Solution(object):
    def areOccurrencesEqual(self, s):
        dic=collections.Counter(s)
        d=list(dic.values())
        return max(d)==min(d)
