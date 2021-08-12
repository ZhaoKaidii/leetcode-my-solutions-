class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ss,c,d=[],0,0
        for i in range(len(s)):
            if s[i] not in ss:
                ss.append(s[i])
                c=len(ss)
                d=max(d,c)
            else:
                while s[i] in ss:
                    ss.pop(0)
                ss.append(s[i])
        return d
