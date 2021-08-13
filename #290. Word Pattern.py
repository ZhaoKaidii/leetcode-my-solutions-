class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d=[]
        dd=""
        s=s+" "
        for i in range(len(s)):
            if s[i]!=" ":
                dd+=s[i]
            else:
                d.append(dd)
                dd=""
        if len(pattern)!=len(d):
            return False
        dic={}
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]]!=d[i]:
                    return False
            else:
                dic[pattern[i]]=d[i]
        dicc={}
        for i in range(len(pattern)):
            if d[i] in dicc:
                if dicc[d[i]]!=pattern[i]:
                    return False
            else:
                dicc[d[i]]=pattern[i]
       
        return True
