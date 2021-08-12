class Solution(object):
    def isUnique(self, astr):
        dic=collections.Counter(astr)
        return len(astr)<2 or max(dic.values())<2
