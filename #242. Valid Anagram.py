class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in t:
            if i in dic:
                dic[i]-=1
            else:
                return False
        ss=list(dic.values())
        return max(ss)==0 and min(ss)==0
