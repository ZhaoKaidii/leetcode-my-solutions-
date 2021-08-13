class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        dicp={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
            if s[i] in dic:
                if dic[s[i]]!=t[i]:
                    return False
        for i in range(len(s)):
            if t[i] not in dicp:
                dicp[t[i]]=s[i]
            if t[i] in dicp:
                if dicp[t[i]]!=s[i]:
                    return False
        return True
