class Solution(object):
    def firstUniqChar(self, s):
        ss=collections.Counter(s)
        for i,ch in enumerate(s):
            if ss[ch]==1:
                return s[i]
        return " "
