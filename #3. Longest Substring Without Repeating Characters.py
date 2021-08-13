class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ss,c=[],0
        for i in s:
            if i not in ss:
                ss.append(i)
                c=max(len(ss),c)           
            else:        
                while i in ss:
                    ss.pop(0)
                ss.append(i)
        return c
