class Solution(object):
    def CheckPermutation(self, s1, s2):
        dic={}
        for i in s1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in s2:
            if i in dic:
                dic[i]-=1
            else:
                return False
        m,n=max(list(dic.values())),min(list(dic.values()))
        return m==n
