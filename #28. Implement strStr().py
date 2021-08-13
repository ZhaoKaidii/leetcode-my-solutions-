class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack)==len(needle):
            return int(haystack==needle)-1
        if len(needle)==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i]==needle[0] and haystack[i:i+len(needle)]==needle:
                return i
        return -1
